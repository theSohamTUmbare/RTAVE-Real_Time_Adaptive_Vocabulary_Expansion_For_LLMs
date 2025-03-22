# **Real-Time Adaptive Vocabulary Expansion for LLMs**

## **Problem Statement**
Medical language models are essential for tasks such as clinical decision support, diagnosis prediction, and research summarization. However, these models often struggle with rapidly evolving medical terminology and emerging domain-specific words. Traditional LLMs rely on static vocabularies, meaning that new or complex terms are usually broken into subtokens—resulting in diluted meaning and reduced comprehension.

The challenge is to enable these models to dynamically update their vocabulary in real time, ensuring both enhanced understanding and, eventually, accurate generation of these terms without compromising existing performance.

---
## **Proposed Solution**
Our approach involves a two-phase adaptive vocabulary expansion method, with a focus on real-time updates:

### **Phase 1: Embedding Table Expansion & Fine-Tuning for Comprehension**
#### **Detection & Data Collection:**
- Automatically identify unknown or emerging medical terms (e.g., from incoming clinical reports or research papers via Google Scholar).
- Collect context-rich data for these terms.

#### **Vocabulary Update (Input Side):**
- Update the tokenizer to treat the new term as a single token.
- Expand the embedding table by adding dedicated embeddings for each new word.
- Example: For a new drug name like `Lecanemab`, add it as a new token and initialize its embedding (using averaging of related terms, external embeddings, or random initialization).

#### **Fine-Tuning:**
- Fine-tune the model on domain-specific data containing these new terms.
- This phase allows the model to learn to understand the new vocabulary while keeping the output softmax layer unchanged.

### **Phase 2: Softmax Layer Expansion & Fine-Tuning for Generation**
#### **Batch-wise Softmax Update:**
- Once a sufficient batch (e.g., 100 new words) has been accumulated, expand the softmax layer by adding new rows corresponding to these words.

#### **Targeted Fine-Tuning:**
- Fine-tune the model on data that includes the new vocabulary.
- Adjust the new softmax weights to align the model’s internal representations with the expanded output space.
- This enables the direct generation of the new terms.

---
## **Novelty**
### **Real-Time Vocabulary Improvement**
Unlike traditional methods that require complete retraining or manual updates, our approach continuously and automatically adapts the vocabulary in real time. The two-phase process—first improving comprehension and then enhancing generation—represents a novel method for real-time dynamic vocabulary expansion in LLMs.

---
## **Benefits**
- **Improved Tokenization and Reduced Ambiguity:**
  - Example: The term `bradykinesia` is treated as a single token, preserving its precise meaning.
- **Enhanced Comprehension of Rare or Emerging Terms:**
  - Example: A novel drug name like `Lecanemab` can be better understood in context.
- **Better Contextual Representation:**
  - Example: Clinical phrases such as `idiopathic pulmonary fibrosis` are processed as unified entities.
- **Enhanced Downstream Task Performance:**
  - Example: Improved responses in medical Q&A systems due to better embeddings.
- **Improved Named Entity Recognition and Information Extraction:**
  - Example: Higher precision in electronic health record analysis.
- **Efficient Adaptation to Evolving Medical Language:**
  - Example: Prompt adaptation to new terminologies without full-scale retraining.

---
## **Challenges**
- **Catastrophic Interference and Model Drift:**
  - Frequent updates risk disrupting established knowledge.
  - Mitigation strategies include gradual fine-tuning and parameter-efficient methods.
- **Integration with Tokenization:**
  - The tokenizer must be updated to recognize multi-word domain-specific terms as single tokens.
- **Computational Overhead:**
  - Continuous vocabulary updates and fine-tuning sessions increase infrastructure complexity.
- **Data Quality and Relevance:**
  - Ensuring high-quality and relevant collected context (e.g., from Google Scholar).
- **Maintaining Consistency Between Input and Output:**
  - Aligning the model’s internal representations with the expanded output (softmax) requires careful fine-tuning.

---
## **Additional Considerations**
- **Evaluation and Monitoring:**
  - Regularly assess the model on both traditional tasks and new domain-specific challenges.
- **Parameter-Efficient Fine-Tuning:**
  - Utilize techniques like LoRA or adapter modules to minimize risks of catastrophic forgetting.
- **Scalability and Batch Management:**
  - Determine optimal batch sizes for softmax expansion to balance adaptation speed and model stability.

---
## **Phase-Wise Plan**

### **Phase 1: Preparation & Setup (Weeks 1–2)**
- **Literature & Technical Review:**
  - Research related work on dynamic vocabulary expansion, medical LLM fine-tuning, and tokenizer modifications.
  - Identify best practices and tools (e.g., Hugging Face Transformers, PyTorch, specific tokenizers).
- **Define Scope & Objectives:**
  - Decide which domain-specific terms to target initially (e.g., novel drug names, emerging conditions).
- **Data Collection:**
  - Gather domain-specific datasets (e.g., open-access medical papers, clinical reports).
- **Environment Setup:**
  - Set up the development environment and experiment tracking.
- **Deliverable:**
  - A project plan document with a literature review summary and an initial dataset.

### **Phase 2: New Word Detection & Embedding Table Expansion (Weeks 3–4)**
- **Modify Tokenizer:**
  - Update the tokenizer vocabulary to add new domain-specific words as single tokens.
- **Embedding Table Expansion:**
  - Develop a script to add new rows to the embedding table for detected words.
- **Integration Testing:**
  - Ensure new words appear correctly in the model’s processing pipeline.
- **Deliverable:**
  - A prototype module for dynamic embedding table expansion.

### **Phase 3: Fine-Tuning for Enhanced Comprehension (Weeks 5–6)**
- **Dataset Preparation:**
  - Curate a dataset enriched with the new domain-specific terms.
- **Fine-Tuning (Phase 1 Focus):**
  - Fine-tune the model on the curated dataset while keeping the softmax unchanged.
- **Evaluation & Analysis:**
  - Evaluate comprehension tasks and compare results to a baseline.
- **Deliverable:**
  - A set of experiments showing improved understanding of new words.

### **Phase 4: (Optional / Stretch Goal) Softmax Layer Expansion & Generation (Weeks 7–8)**
- **Batch-wise Softmax Update:**
  - Expand the softmax layer after accumulating a batch of new words.
- **Targeted Fine-Tuning for Generation:**
  - Fine-tune the model to align internal representations with the expanded output layer.
- **Final Evaluation & Reporting:**
  - Evaluate performance and document findings.
- **Deliverable:**
  - A demo, progress report, and documentation detailing challenges and future directions.

---
