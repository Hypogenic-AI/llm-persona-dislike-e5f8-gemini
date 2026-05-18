# Resources Catalog

## Summary
This document catalogs all resources gathered for the research into persona-persona dislike in LLMs. These resources include academic papers, datasets for persona and preference modeling, and utility code for analysis.

## Papers
Total papers downloaded: 5

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| Us-vs-Them bias in Large Language Models | Prama et al. | 2025 | [2512.13699v1...pdf](papers/2512.13699v1_UsvsThem_bias_in_Large_Language_Models.pdf) | Investigates ingroup/outgroup bias across personas. |
| Persona Setting Pitfall | Dong et al. | 2024 | [2409.03843v1...pdf](papers/2409.03843v1_Persona_Setting_Pitfall_Persistent_Outgroup_Biases_in_Large_Language_Models.pdf) | Explores how identity adoption causes outgroup bias. |
| I Am Not Them | Dong et al. | 2024 | [2402.10436v1...pdf](papers/2402.10436v1_I_Am_Not_Them_Fluid_Identities_and_Persistent_Outgroup_Bias_in_Large_Language_Models.pdf) | Highlights persistent outgroup bias in social identities. |
| Evaluating Biases in Persona-Steered Gen | Liu et al. | 2024 | [2405.20253v1...pdf](papers/2405.20253v1_Evaluating_Large_Language_Model_Biases_in_PersonaSteered_Generation.pdf) | Analyzes biases in persona-steered LLM generation. |
| Are Social Sentiments Inherent in LLMs? | Tanaka et al. | 2024 | [2408.04293v1...pdf](papers/2408.04293v1_Are_Social_Sentiments_Inherent_in_LLMs.pdf) | Extracts inter-demographic sentiments from LLMs. |

See `literature_review.md` for detailed synthesis.

## Datasets
Total datasets gathered: 2

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| Nemotron-Personas-USA | NVIDIA (HuggingFace) | 100 samples (sampled) | Persona modeling | [datasets/nemotron_personas/](datasets/nemotron_personas/) | Extremely rich personas with hobbies, values, and goals. |
| Value_Alignment_Tax | Tinyhope (HuggingFace) | 100 samples (sampled) | Value trade-offs | [datasets/value_alignment_tax/](datasets/value_alignment_tax/) | Useful for testing value alignment and divergence. |

### Dataset Download Instructions
The datasets are sampled for local inspection. To download the full datasets, use the following commands in the virtual environment:

```python
from datasets import load_dataset
# Nemotron Personas
ds_nemotron = load_dataset('nvidia/Nemotron-Personas-USA')
# Value Alignment Tax
ds_value = load_dataset('Tinyhope/Value_Alignment_Tax')
```

## Code Repositories
Total repositories cloned: 2

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| py-allotax | https://github.com/compstorylab/py-allotax | Rank-turbulence divergence | [code/py-allotax/](code/py-allotax/) | Tool for comparing word usage across groups. |
| shifterator | https://github.com/ryanjgallagher/shifterator | Word shift analysis | [code/shifterator/](code/shifterator/) | Tool for visualizing sentiment and frequency shifts. |

## Resource Gathering Notes

### Search Strategy
- Used `paper-finder` for diligent academic search (arXiv, Semantic Scholar).
- Used `huggingface_hub` for dataset discovery.
- Used `google_web_search` to find specific researcher repositories.

### Challenges Encountered
- ArXiv API rate limiting (HTTP 429) required implementing delays between requests.
- Some specific experimental code from very recent papers (late 2025) is not yet public or indexed.

### Recommendations for Experiment Design
1.  **Primary Dataset**: `Nemotron-Personas-USA` provides high-fidelity personas that allow for non-political preference divergence testing (e.g., comparing a "routine-obsessed food service worker" with a "spontaneous artist").
2.  **Baseline**: Use the default model response as the neutral baseline.
3.  **Metrics**: Use the "Us-vs-Them" scoring rubric from Prama et al. (2025) and sentiment shift visualization from `shifterator`.
4.  **Hypothesis Test**: Specifically test if Persona A's "like" of X predicts Persona B's "dislike" of X if Persona B is defined in opposition to Persona A's broader traits.
