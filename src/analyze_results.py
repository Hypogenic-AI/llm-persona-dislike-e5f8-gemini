import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr

def analyze_reciprocal():
    with open('results/evaluation_results.json', 'r') as f:
        data = json.load(f)
    
    records = []
    for entry in data:
        eval_uuid = entry['evaluator_uuid']
        target_uuid = entry['target_uuid']
        distance = entry['distance']
        
        ratings = [e['rating'] for e in entry['evaluations']]
        avg_rating = np.mean(ratings)
        
        # Split by likes and dislikes of target
        # First 5 were "I like...", next 5 were "I dislike..."
        like_ratings = [e['rating'] for e in entry['evaluations'][:5]]
        dislike_ratings = [e['rating'] for e in entry['evaluations'][5:]]
        
        records.append({
            'evaluator': eval_uuid,
            'target': target_uuid,
            'distance': distance,
            'avg_rating': avg_rating,
            'avg_like_rating': np.mean(like_ratings),
            'avg_dislike_rating': np.mean(dislike_ratings),
            'is_self': eval_uuid == target_uuid
        })
        
    df = pd.DataFrame(records)
    
    # Exclude self-evaluations for correlation
    df_others = df[~df['is_self']]
    
    corr_p, p_val_p = pearsonr(df_others['distance'], df_others['avg_rating'])
    corr_s, p_val_s = spearmanr(df_others['distance'], df_others['avg_rating'])
    
    print(f"Correlation (Pearson) between distance and avg rating: {corr_p:.4f} (p={p_val_p:.4f})")
    print(f"Correlation (Spearman) between distance and avg rating: {corr_s:.4f} (p={p_val_s:.4f})")
    
    # Visualizations
    plt.figure(figsize=(10, 6))
    sns.regplot(data=df_others, x='distance', y='avg_rating')
    plt.title('Persona Distance vs. Preference Agreement')
    plt.xlabel('Cosine Distance between Personas')
    plt.ylabel('Average Agreement Rating (1-5)')
    plt.savefig('figures/distance_vs_rating.png')
    
    # Self vs Others
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='is_self', y='avg_rating')
    plt.title('Agreement: Self vs. Others')
    plt.xticks([0, 1], ['Others', 'Self'])
    plt.savefig('figures/self_vs_others.png')
    
    return df

def analyze_schismogenesis():
    with open('results/schismogenesis_results.json', 'r') as f:
        data = json.load(f)
    
    all_ratings = []
    for entry in data:
        ratings = [e['rating'] for e in entry['opposite_evals']]
        all_ratings.extend(ratings)
        
    avg_rating = np.mean(all_ratings)
    print(f"\nAverage rating for 'Opposite Persona' on target's likes: {avg_rating:.4f}")
    print(f"Percentage of ratings <= 2 (Dislike): {np.mean(np.array(all_ratings) <= 2) * 100:.2f}%")
    
    # Show some examples of schismogenesis
    print("\nSchismogenesis Examples:")
    for entry in data[:2]:
        print(f"Persona A: {entry['persona_a_desc'][:100]}...")
        for eval in entry['opposite_evals'][:2]:
            print(f"  Item: {eval['item']}, Rating: {eval['rating']}")
            print(f"  Justification: {eval['justification']}")

def main():
    df = analyze_reciprocal()
    analyze_schismogenesis()

if __name__ == "__main__":
    main()
