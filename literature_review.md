# Literature Review: Persona-Persona Dislike in LLMs

## Research Area Overview
Large Language Models (LLMs) are increasingly recognized not just as static knowledge bases, but as systems capable of adopting distinct "personas" or "social identities." This literature review explores how these persona-conditioned LLMs exhibit "us-versus-them" dynamics, specifically focusing on the tendency for personas with divergent preferences to exhibit mutual dislike or opposition.

## Key Papers

### 1. Us-vs-Them bias in Large Language Models (Prama et al., 2025)
- **Source**: arXiv:2512.13699
- **Key Contribution**: Quantifies "ingroup solidarity" and "outgroup hostility" across multiple LLM architectures (GPT-4.1, LLaMA-3.1, etc.).
- **Methodology**: Used "We are" (ingroup) and "They are" (outgroup) prompts. Analyzed sentiment shifts and semantic divergence using allotaxonometry and embedding regression.
- **Results**: Found consistent ingroup favoritism and outgroup derogation. Conservative personas showed higher outgroup hostility, while liberal personas showed stronger ingroup solidarity.
- **Relevance**: Directly supports the "dislike" part of the hypothesis and provides a robust measurement framework.

### 2. Persona Setting Pitfall: Persistent Outgroup Biases in Large Language Models Arising from Social Identity Adoption (Dong et al., 2024)
- **Source**: arXiv:2409.03843
- **Key Contribution**: Highlights that assigning a persona leads LLMs to internalize social identity biases, with outgroup bias being as strong as ingroup favoritism.
- **Methodology**: Used psychological batteries (Likert scales) and the Political Compass test to map value alignments.
- **Results**: Confirmed that LLMs emulate human-like "partisan sorting," where identities (race, gender, religion) align with partisan views and lead to reciprocal opposition.
- **Relevance**: Connects persona adoption to active rejection (dislike) of outgroup values.

### 3. I Am Not Them: Fluid Identities and Persistent Out-group Bias in Large Language Models (Dong et al., 2024)
- **Source**: arXiv:2402.10436
- **Key Contribution**: Investigates how social identity adoption triggers negativity toward outgroups that exceeds positivity toward ingroups.
- **Relevance**: Emphasizes that "dislike" (outgroup bias) is a dominant feature of persona-conditioned behavior.

### 4. Are Social Sentiments Inherent in LLMs? An Empirical Study on Extraction of Inter-demographic Sentiments (Tanaka et al., 2024)
- **Source**: arXiv:2408.04293
- **Key Contribution**: Validates that LLMs encode "inter-group sentiments" (how one group feels about another) that reflect real-world social surveys.
- **Relevance**: Shows that LLMs have a "map" of social sentiments that includes mutual dislikes.

### 5. Evaluating Large Language Model Biases in Persona-Steered Generation (Liu et al., 2024)
- **Source**: arXiv:2405.20253
- **Key Contribution**: Examines how steering LLMs toward specific personas amplifies existing societal biases and affects downstream tasks.

## Common Methodologies
1.  **Sentence Completion**: Prompting with "We are..." and "They are..." to elicit identity-based sentiments.
2.  **Likert Scale Evaluation**: Asking models to express agreement with value-laden statements from the perspective of a persona.
3.  **Embedding Regression**: Analyzing shifts in contextual embeddings to quantify semantic divergence between personas.
4.  **Allotaxonometry**: Using rank-turbulence divergence to compare word usage frequencies between "us" and "them" narratives.

## Standard Baselines
- **Default Persona**: The model's behavior without explicit persona conditioning.
- **Opposing Personas**: Direct comparison between divergent personas (e.g., Liberal vs. Conservative, Pro-Choice vs. Pro-Life).

## Gaps and Opportunities
- Most research focuses on **political** or **demographic** personas. There is a gap in exploring **preference-based** personas (e.g., aesthetic tastes, technical preferences) and whether "opposition" emerges from pure preference divergence.
- The concept of "schismogenesis" (definition-by-contrast) in LLMs is theorized but not explicitly tested as a mechanism for persona creation.

## Recommendations for Our Experiment
1.  **Use Preference-Based Personas**: Move beyond politics to see if divergent tastes (e.g., in art, music, or lifestyle) trigger similar "Us-vs-Them" dynamics.
2.  **Reciprocal Evaluation**: Have Persona A evaluate the preferences of Persona B and vice versa.
3.  **Measurement**: Combine sentiment analysis (labMT/VADER) with "outgroup hostility" scoring using an LLM judge.
4.  **Dataset**: Utilize the `Nemotron-Personas-USA` dataset to source rich, multifaceted personas for the experiment.
