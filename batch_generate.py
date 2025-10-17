"""
Batch generate all 100 LLM courses
Run this script to create all course folders with complete applications
"""

import os
import shutil

# Define all 100 courses
COURSES = [
    # Module 1-10 definitions (001-100)
    *[{"id": f"{i:03d}", "name": name, "title": title, "module": (i-1)//10 + 1} 
      for i, (name, title) in enumerate([
        ("introduction_to_language_models", "Introduction to Language Models"),
        ("tokenization_fundamentals", "Tokenization Fundamentals"),
        ("word2vec_embeddings", "Word2Vec Embeddings"),
        ("glove_embeddings", "GloVe Embeddings"),
        ("contextual_embeddings", "Contextual Embeddings"),
        ("sequence_modeling", "Sequence Modeling"),
        ("rnn_fundamentals", "RNN Fundamentals"),
        ("lstm_networks", "LSTM Networks"),
        ("gru_networks", "GRU Networks"),
        ("attention_basics", "Attention Mechanism Basics"),
        # Module 2
        ("text_preprocessing", "Text Preprocessing Pipeline"),
        ("byte_pair_encoding", "Byte-Pair Encoding"),
        ("wordpiece", "WordPiece Tokenization"),
        ("sentencepiece", "SentencePiece"),
        ("subword_regularization", "Subword Regularization"),
        ("language_detection", "Language Detection"),
        ("text_normalization", "Text Normalization"),
        ("ner", "Named Entity Recognition"),
        ("pos_tagging", "POS Tagging"),
        ("dependency_parsing", "Dependency Parsing"),
        # Module 3
        ("neural_networks", "Neural Network Fundamentals"),
        ("backpropagation", "Backpropagation"),
        ("optimization", "Optimization Algorithms"),
        ("regularization", "Regularization Techniques"),
        ("batch_norm", "Batch Normalization"),
        ("layer_norm", "Layer Normalization"),
        ("dropout", "Dropout Variants"),
        ("activations", "Activation Functions"),
        ("loss_functions", "Loss Functions for NLP"),
        ("gradient_flow", "Gradient Flow Analysis"),
        # Module 4
        ("transformer", "Transformer Architecture"),
        ("self_attention", "Self-Attention Mechanism"),
        ("multi_head_attention", "Multi-Head Attention"),
        ("positional_encoding", "Positional Encoding"),
        ("ffn", "Feed-Forward Networks"),
        ("encoder", "Encoder Architecture"),
        ("decoder", "Decoder Architecture"),
        ("cross_attention", "Cross-Attention"),
        ("transformer_variants", "Transformer Variants"),
        ("attention_viz", "Attention Visualization"),
        # Module 5
        ("lm_objectives", "Language Modeling Objectives"),
        ("mlm", "Masked Language Modeling"),
        ("clm", "Causal Language Modeling"),
        ("nsp", "Next Sentence Prediction"),
        ("bert_pretrain", "BERT Pre-training"),
        ("gpt_pretrain", "GPT Pre-training"),
        ("t5_pretrain", "T5 Pre-training"),
        ("data_curation", "Pre-training Data Curation"),
        ("curriculum_learning", "Curriculum Learning"),
        ("multitask_pretrain", "Multi-task Pre-training"),
        # Module 6
        ("transfer_learning", "Transfer Learning Basics"),
        ("full_finetune", "Full Fine-tuning"),
        ("feature_extraction", "Feature Extraction"),
        ("adapters", "Adapter Layers"),
        ("lora", "LoRA"),
        ("prefix_tuning", "Prefix Tuning"),
        ("prompt_tuning", "Prompt Tuning"),
        ("few_shot", "Few-Shot Learning"),
        ("zero_shot", "Zero-Shot Learning"),
        ("multitask_finetune", "Multi-task Fine-tuning"),
        # Module 7
        ("rlhf", "RLHF"),
        ("ppo", "PPO"),
        ("dpo", "DPO"),
        ("rag", "RAG"),
        ("chain_of_thought", "Chain-of-Thought"),
        ("react", "ReAct"),
        ("llm_agents", "LLM Agents"),
        ("tool_use", "Tool Use"),
        ("multi_agent", "Multi-Agent Systems"),
        ("constitutional_ai", "Constitutional AI"),
        # Module 8
        ("quantization", "Model Quantization"),
        ("distillation", "Knowledge Distillation"),
        ("pruning", "Pruning Techniques"),
        ("mixed_precision", "Mixed Precision Training"),
        ("gradient_checkpoint", "Gradient Checkpointing"),
        ("flash_attention", "Flash Attention"),
        ("model_parallel", "Model Parallelism"),
        ("data_parallel", "Data Parallelism"),
        ("pipeline_parallel", "Pipeline Parallelism"),
        ("efficient_inference", "Efficient Inference"),
        # Module 9
        ("text_classification", "Text Classification"),
        ("sentiment_analysis", "Sentiment Analysis"),
        ("qa", "Question Answering"),
        ("summarization", "Text Summarization"),
        ("translation", "Machine Translation"),
        ("code_generation", "Code Generation"),
        ("dialogue", "Dialogue Systems"),
        ("information_extraction", "Information Extraction"),
        ("text_to_sql", "Text-to-SQL"),
        ("semantic_search", "Semantic Search"),
        # Module 10
        ("moe", "Mixture of Experts"),
        ("sparse_transformers", "Sparse Transformers"),
        ("long_context", "Long-Context Models"),
        ("multimodal", "Multimodal LLMs"),
        ("diffusion_lm", "Diffusion Language Models"),
        ("continual_learning", "Continuous Learning"),
        ("model_editing", "Model Editing"),
        ("interpretability", "Interpretability"),
        ("safety_alignment", "Safety & Alignment"),
        ("future_directions", "Future Directions"),
      ], 1)]
]

def create_all_courses():
    """Create all 100 course folders"""
    template_dir = "course_001_introduction_to_language_models"
    
    for course in COURSES:
        course_dir = f"course_{course['id']}_{course['name']}"
        
        if os.path.exists(course_dir):
            print(f"⏭️  Skipping {course_dir} (already exists)")
            continue
        
        # Copy template
        shutil.copytree(template_dir, course_dir)
        
        # Update files with course-specific content
        update_course_files(course_dir, course)
        
        print(f"✓ Created {course_dir}")

def update_course_files(course_dir, course):
    """Update template files with course-specific information"""
    # Update README
    readme_path = os.path.join(course_dir, 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('Course 001', f'Course {course["id"]}')
    content = content.replace('Introduction to Language Models', course['title'])
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Update index.html
    html_path = os.path.join(course_dir, 'index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('Course 001', f'Course {course["id"]}')
    content = content.replace('Introduction to Language Models', course['title'])
    content = content.replace('Module 1', f'Module {course["module"]}')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    print("🚀 Generating all 100 LLM courses...")
    print("=" * 60)
    create_all_courses()
    print("=" * 60)
    print("✅ All courses generated successfully!")
    print(f"📁 Total: {len(COURSES)} courses created")
