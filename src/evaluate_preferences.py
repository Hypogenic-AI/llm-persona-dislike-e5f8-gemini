import json
import os
import numpy as np
import pandas as pd
from openai import OpenAI
from tqdm import tqdm

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_preferences(evaluator_persona, target_preferences):
    prompt = f"""You are the following persona:
{evaluator_persona}

You will be presented with a list of statements about someone else's preferences (things they like or dislike).
For each statement, provide your personal reaction as this persona.
Rate each statement on a scale of 1 to 5:
1: Strong Disagreement / Dislike of this preference
2: Disagreement / Slight Dislike
3: Neutral / Indifferent
4: Agreement / Slight Like
5: Strong Agreement / Love of this preference

Also provide a brief one-sentence justification for each rating from your persona's perspective.

Statements:
{json.dumps(target_preferences, indent=2)}

Output JSON format:
{{
  "evaluations": [
    {{
      "statement": "...",
      "rating": 1-5,
      "justification": "..."
    }},
    ...
  ]
}}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content)

def main():
    if not os.path.exists('results/persona_distances.json') or not os.path.exists('results/persona_preferences.json'):
        print("Missing required input files.")
        return

    with open('results/persona_distances.json', 'r') as f:
        dist_data = json.load(f)
    with open('results/persona_preferences.json', 'r') as f:
        pref_data = json.load(f)
        
    uuids = list(pref_data.keys())
    dist_matrix = np.array(dist_data['distance_matrix'])
    uuid_to_idx = {uuid: i for i, uuid in enumerate(dist_data['uuids'])}
    
    subset_uuids = uuids[:20]
    uuid_to_idx_subset = {uuid: i for i, uuid in enumerate(subset_uuids)}
    
    results = []
    # We'll evaluate a sample of pairs for each of 10 personas
    subset_evaluators = subset_uuids[:10]
    
    for i, uuid_a in enumerate(tqdm(subset_evaluators, desc="Evaluators")):
        p_a = pref_data[uuid_a]['persona_info']
        desc_a = f"{p_a['persona']} {p_a['cultural_background']} {p_a['professional_persona']}"

        idx_a_full = uuid_to_idx[uuid_a]
        distances_full = dist_matrix[idx_a_full]
        
        # Get distances only to our subset
        subset_indices_full = [uuid_to_idx[u] for u in subset_uuids]
        subset_distances = distances_full[subset_indices_full]
        
        # Sort indices within the subset
        sorted_subset_indices = np.argsort(subset_distances)
        
        # Mapping back to subset_uuids indices
        idx_a_subset = uuid_to_idx_subset[uuid_a]
        other_indices_subset = [idx for idx in sorted_subset_indices if idx != idx_a_subset]

        targets_subset = [idx_a_subset] # Self
        targets_subset.extend(other_indices_subset[:2]) # Close
        targets_subset.extend(other_indices_subset[-2:]) # Far
        mid = len(other_indices_subset) // 2
        targets_subset.extend(other_indices_subset[mid:mid+1]) # Medium
        
        targets_subset = list(dict.fromkeys(targets_subset))

        for idx_b_subset in targets_subset:
            uuid_b = subset_uuids[idx_b_subset]
            p_b_prefs = pref_data[uuid_b]['preferences']
            all_statements = [f"I like {p}" for p in p_b_prefs['likes']] + [f"I dislike {p}" for p in p_b_prefs['dislikes']]
            
            idx_b_full = uuid_to_idx[uuid_b]
            distance = dist_matrix[idx_a_full][idx_b_full]
            
            try:
                evals = evaluate_preferences(desc_a, all_statements)
                results.append({
                    'evaluator_uuid': uuid_a,
                    'target_uuid': uuid_b,
                    'distance': distance,
                    'evaluations': evals['evaluations']
                })
            except Exception as e:
                print(f"Error evaluating {uuid_a} -> {uuid_b}: {e}")
                
    with open('results/evaluation_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Saved {len(results)} evaluations to results/evaluation_results.json")

if __name__ == "__main__":
    main()
