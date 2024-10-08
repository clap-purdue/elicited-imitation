- The `gricean_pragmatics` project includes several scripts, algorithms, and metrics to evaluating LLMs’ pragmatic competence in multilingual settings 

## Naturalness:

Naturalness Metric Explanation:
utterance_surprisal: The surprisal score for the given utterance.
interpretation_a_surprisal: The surprisal score for interpretation (a) ("He is very smart").
interpretation_b_surprisal: The surprisal score for interpretation (b) ("He is not smart at all").
The function calculates the absolute difference in surprisal scores between the utterance and each interpretation.
The output dictionary contains:
difference_a: The difference between the utterance and interpretation (a).
difference_b: The difference between the utterance and interpretation (b).
preferred_interpretation: The interpretation with the smaller surprisal difference, 
indicating the LLM’s preferred implied meaning.
This function allows us to evaluate whether the LLMs show pragmatic sensitivity by comparing surprisal scores.


## Sensitivity to different Shades of Meaning (SSM):

SSM metric Explanation:
- embedding_a: The embedding for the first sentence (e.g., "Alex was not unaware of the issue").
- embedding_b: The embedding for the second sentence (e.g., "Alex was slightly aware of the issue").
- embedding_c: The embedding for the third sentence (e.g., "Alex was aware of the issue").
- The function computes cosine similarities between sentence pairs:
   - similarity_ab: Similarity between sentence A and B.
   - similarity_bc: Similarity between sentence B and C.
- The function then ranks these similarities in descending order.
- The output dictionary contains:
   - similarity_ab: Cosine similarity between sentence A and B.
   - similarity_bc: Cosine similarity between sentence B and C.
   - ranking: The ranked list of similarities, indicating which sentence pair is more similar.


## Pragmatic Reasoning Chains (PRC):

PRC metrics explanation

To evaluate the PRC metric, we define:

1. Reasoning Step Prompts: These will be custom prompts based on formal reasoning steps that the LLM should follow.
2. Expected Reasoning Steps: The correct reasoning steps according to formal pragmatics.
3. LLM Output Analysis: The comparison between the LLM's generated steps and the expected steps.

- LLM Responses: These are the reasoning steps generated by the LLM when probed with specific prompts.
- Expected Steps: These represent the correct reasoning steps based on formal pragmatics (e.g., deriving "not all" from "some").
- Accuracy: The overall accuracy of the LLM’s responses is calculated as the proportion of correctly generated reasoning steps.
- Step Scores: This array represents the correctness of each individual step (1.0 for correct, 0.0 for incorrect).

### Additional Enhancements:

- Partial Matching: You could implement a more sophisticated comparison, allowing partial credit for reasoning steps that are conceptually correct but not exactly matching the expected step.
- Prompt Engineering: You can design prompts that explicitly probe each reasoning step, providing more granular control over the evaluation process.
- Multilingual Capability: By altering the `expected_steps` and `llm_responses` according to different languages, the function can evaluate PRC in a multilingual context.

This approach allows us to systematically evaluate how well LLMs follow complex pragmatic reasoning processes, aligning with formal pragmatic frameworks.

## Implicature Recovery Rate (IRR):

IRR metric Explanation:
Explanation:
successful_recoveries: The number of implicature errors that were successfully recovered by the LLM after introducing noise or ambiguity.
total_errors: The total number of implicature errors introduced during the evaluation.
The function calculates the IRR as the ratio of successful_recoveries to total_errors.
The output is a floating-point number representing the IRR, 
which can be interpreted as a percentage (e.g., 0.60 means 60% of implicatures were successfully recovered).
This function allows us to 
evaluate the robustness of LLMs in handling and resolving implicature-related ambiguities 
by measuring how well they can recover from initial errors.


## Pragmatic Sensitivity Index (PSI):

PSI metric Explanation:
original_accuracy: The accuracy of the LLM's responses when provided with the original context.
changed_accuracy: The accuracy of the LLM's responses after subtle contextual changes, 
such as scrambling nouns or replacing key words with nonsense words.
The function calculates the PSI as the difference between original_accuracy and changed_accuracy.
A higher PSI indicates greater sensitivity to contextual changes, 
meaning the model's performance drops more when the context is altered.
This function allows us to evaluate how well LLMs can adjust to subtle shifts in context, 
reflecting their pragmatic sensitivity.
