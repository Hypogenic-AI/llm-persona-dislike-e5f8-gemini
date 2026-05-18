# Research Report: Do LLMs model persona-persona dislike?

## 1. Executive Summary
This research investigated whether Large Language Models (LLMs) capture the relational structure of persona-persona dislike. We hypothesized that personas far apart in a multidimensional "persona space" would express more dislike for each other's preferences, reflecting human social dynamics where distinction is often defined through opposition. Using the `Nemotron-Personas-USA` dataset and GPT-4o-mini, we demonstrated a statistically significant negative correlation ($r = -0.49$, $p < 0.001$) between persona distance (measured via embedding cosine distance) and reciprocal preference agreement. Furthermore, we showed that LLMs can perform "zero-shot schismogenesis," where adopting an "opposite" persona leads to the systematic rejection of the target's specific likes (88% rejection rate).

## 2. Research Question & Motivation
**Hypothesis:** LLMs do not just model isolated persona traits but also encode the relational logic of opposition. Personas with divergent values and lifestyles are modeled as having mutual antipathy for each other's tastes.

**Importance:** As LLMs are increasingly used in multi-agent simulations and social modeling, understanding if they inherently capture "us-vs-them" dynamics at a granular preference level is crucial. This has implications for polarization modeling and the design of cooperative AI systems.

## 3. Methodology
- **Data:** 20 multifaceted personas sampled from `Nemotron-Personas-USA`.
- **Persona Distance:** Computed using `all-MiniLM-L6-v2` embeddings of full persona descriptions (persona summary + cultural background + professional bio).
- **Preference Generation:** For each persona, GPT-4o-mini generated 5 specific likes and 5 specific dislikes based on their description.
- **Reciprocal Evaluation:** 10 "Evaluator" personas were prompted to adopt their persona and rate their agreement (1-5 Likert scale) with the preferences of 6 target personas (Self, 2 Close, 2 Far, 1 Medium).
- **Schismogenesis Test:** The model was told it was the "complete opposite" of a target persona and asked to evaluate the target's likes.
- **Metrics:** Pearson/Spearman correlation between persona distance and average rating; rejection rate in schismogenesis.

## 4. Results
### Distance-Dislike Correlation
We found a strong and significant negative correlation between the distance between two personas and how much they agreed with each other's preferences.

| Metric | Correlation | p-value |
|--------|-------------|---------|
| Pearson $r$ | -0.4913 | 0.0003 |
| Spearman $\rho$ | -0.5219 | 0.0001 |

- **Self-Agreement (Baseline):** Personas evaluating their own preferences had a much higher average agreement ($\mu \approx 4.5$) compared to evaluating others.
- **Outgroup Disagreement:** Personas at the maximum distance frequently gave ratings of 1 or 2 to the other's preferences, often justifying it through the contrast in their values (e.g., "I find rigid organization stifling" vs "I thrive in creative chaos").

### Schismogenesis
When instructed to be the "opposite" of a target, the model demonstrated a remarkable ability to invert preferences.
- **Average Rating for Likes:** 1.76 (on a 1-5 scale).
- **Rejection Rate (Rating $\le$ 2):** 88%.

## 5. Analysis & Discussion
The results support the idea that LLMs have a "social map" where distance translates into perceived opposition. This goes beyond simple sentiment; the justifications provided by the model shows it understands *why* certain personas would clash. For example, a "routine-obsessed" persona was consistently modeled as disliking the "spontaneous" preferences of an artistic persona.

The "zero-shot schismogenesis" results are particularly striking as they show that the "opposite" relationship is structurally encoded. The model doesn't just "dislike everything"; it constructs a counter-identity that specifically negates the target's values.

## 6. Limitations
- **Sample Size:** Due to time constraints, we only used a subset of 20 personas and 10 evaluators.
- **Model Choice:** We used GPT-4o-mini; results might vary with larger or different model families (e.g., Llama, Claude).
- **Embedding Simplification:** Cosine distance of text embeddings is a proxy for "social distance" but might miss specific dimensions of conflict (e.g., status, power).

## 7. Conclusions & Next Steps
LLMs do indeed model persona-persona dislike as a function of their distance in persona space. They capture the relational and oppositional nature of identity. 
**Future Work:**
- Investigate if "fine-grained" distance (e.g., distance in specific domains like 'Arts' vs 'Politics') predicts dislike differently.
- Test if LLMs can find "common ground" between distant personas when specifically prompted to do so.
- Explore the "asymmetry" of dislike (e.g., does a high-status persona dislike a low-status one more than vice-versa?).

## Figures
- `figures/distance_vs_rating.png`: Scatter plot showing the negative correlation.
- `figures/self_vs_others.png`: Box plot comparing self-agreement to outgroup agreement.
