import json
import os
from openai import OpenAI
from tqdm import tqdm

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_preferences(persona_desc):
    prompt = f"""Based on the following persona description, generate a list of 10 specific preferences. 
5 things they likely LOVE and 5 things they likely DISLIKE or are ANNoyed by.
Be specific and nuanced, going beyond the obvious.

Persona: {persona_desc}

Output JSON format:
{{
  "likes": ["pref1", "pref2", "pref3", "pref4", "pref5"],
  "dislikes": ["pref6", "pref7", "pref8", "pref9", "pref10"]
}}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={ "type": "json_object" }
    )
    return json.loads(response.choices[0].message.content)

def main():
    with open('datasets/nemotron_personas/samples.json', 'r') as f:
        personas = json.load(f)
    
    # Select a subset of 20 personas
    subset = personas[:20]
    
    preference_data = {}
    for p in tqdm(subset):
        uuid = p['uuid']
        desc = f"{p['persona']} {p['cultural_background']} {p['professional_persona']}"
        prefs = generate_preferences(desc)
        preference_data[uuid] = {
            'persona_info': p,
            'preferences': prefs
        }
        
    with open('results/persona_preferences.json', 'w') as f:
        json.dump(preference_data, f, indent=2)

if __name__ == "__main__":
    main()
