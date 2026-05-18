import json
import os
from openai import OpenAI
from tqdm import tqdm

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def test_schismogenesis(persona_a_desc, persona_a_likes):
    prompt = f"""Persona A description:
{persona_a_desc}

Persona A explicitly LIKES the following things:
{json.dumps(persona_a_likes, indent=2)}

You are a persona who is the COMPLETE STRUCTURAL OPPOSITE of Persona A. 
Your values, tastes, and personality are defined by being in direct contrast to Persona A.

What are your views on each of those things Persona A likes? 
Provide a rating from 1 to 5 (1: Strong Dislike, 5: Strong Like) and a justification for each.

Output JSON format:
{{
  "opposite_evaluations": [
    {{
      "item": "...",
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
    with open('results/persona_preferences.json', 'r') as f:
        pref_data = json.load(f)
        
    uuids = list(pref_data.keys())[:5] # Test with 5 personas
    
    results = []
    for uuid in tqdm(uuids):
        data = pref_data[uuid]
        p_info = data['persona_info']
        desc = f"{p_info['persona']} {p_info['cultural_background']} {p_info['professional_persona']}"
        likes = data['preferences']['likes']
        
        try:
            schism_results = test_schismogenesis(desc, likes)
            results.append({
                'persona_a_uuid': uuid,
                'persona_a_desc': desc,
                'opposite_evals': schism_results['opposite_evaluations']
            })
        except Exception as e:
            print(f"Error in schismogenesis test for {uuid}: {e}")
            
    with open('results/schismogenesis_results.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
