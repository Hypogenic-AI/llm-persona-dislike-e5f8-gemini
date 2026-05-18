import json
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

def load_personas(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_embeddings(texts, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings

def main():
    persona_file = 'datasets/nemotron_personas/samples.json'
    personas = load_personas(persona_file)
    
    # Use the full 'persona' field which is a summary, plus cultural background for more context
    texts = [f"{p['persona']} {p['cultural_background']}" for p in personas]
    names = [p.get('uuid', str(i)) for i, p in enumerate(personas)]
    
    print(f"Generating embeddings for {len(texts)} personas...")
    embeddings = get_embeddings(texts)
    
    # Compute similarity matrix
    similarity_matrix = cosine_similarity(embeddings)
    distance_matrix = 1 - similarity_matrix
    
    # Save results
    results = {
        'uuids': names,
        'similarity_matrix': similarity_matrix.tolist(),
        'distance_matrix': distance_matrix.tolist()
    }
    
    with open('results/persona_distances.json', 'w') as f:
        json.dump(results, f)
        
    print("Distance matrix saved to results/persona_distances.json")

    # Find some interesting pairs
    # Copy distance matrix to avoid modifying original
    dist_copy = distance_matrix.copy()
    
    # Most similar (excluding self)
    np.fill_diagonal(dist_copy, np.inf)
    min_idx = np.unravel_index(np.argmin(dist_copy), dist_copy.shape)
    print(f"Most similar pair: {names[min_idx[0]]} and {names[min_idx[1]]} (dist: {dist_copy[min_idx]:.4f})")
    print(f"P1: {texts[min_idx[0]][:200]}...")
    print(f"P2: {texts[min_idx[1]][:200]}...")
    
    # Most dissimilar
    # Replace inf back with 0 for finding max if diagonal was inf
    dist_copy_max = distance_matrix.copy()
    np.fill_diagonal(dist_copy_max, -np.inf)
    max_idx = np.unravel_index(np.argmax(dist_copy_max), dist_copy_max.shape)
    print(f"\nMost dissimilar pair: {names[max_idx[0]]} and {names[max_idx[1]]} (dist: {dist_copy_max[max_idx]:.4f})")
    print(f"P1: {texts[max_idx[0]][:200]}...")
    print(f"P2: {texts[max_idx[1]][:200]}...")

if __name__ == "__main__":
    main()
