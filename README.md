# Persona-Persona Dislike in LLMs

This research investigates whether Large Language Models (LLMs) model the relational aspect of persona dislike—specifically, whether personas far apart in "persona space" are more likely to dislike each other's preferences.

## Key Findings
- **Distance-Dislike Correlation:** We found a significant negative correlation ($r = -0.49$, $p < 0.001$) between the embedding-based distance of two personas and their mutual preference agreement.
- **Zero-Shot Schismogenesis:** LLMs can systematically invert preferences when adopted an "opposite" persona, demonstrating a structural understanding of persona-based opposition (88% rejection rate).
- **Nuanced Justification:** LLMs provide coherent, persona-driven justifications for disliking outgroup preferences (e.g., a structured persona rejecting "creative chaos").

## Reproduction
1.  **Environment:** Create a virtual environment and install dependencies:
    ```bash
    uv venv .venv
    source .venv/bin/activate
    uv pip install pandas numpy matplotlib seaborn scikit-learn sentence-transformers openai datasets vaderSentiment tqdm scipy
    ```
2.  **API Key:** Set your `OPENAI_API_KEY` in the environment.
3.  **Run Experiments:**
    ```bash
    python src/persona_distance.py
    python src/generate_preferences.py
    python src/evaluate_preferences.py
    python src/schismogenesis_test.py
    python src/analyze_results.py
    ```

## File Structure
- `src/`: Experimental scripts.
- `results/`: Intermediate data and JSON results.
- `figures/`: Visualizations of the findings.
- `REPORT.md`: Full research report.

## License
MIT
