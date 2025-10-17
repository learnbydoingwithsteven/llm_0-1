# Course 041: Language Modeling Objectives

## 🎯 Learning Objectives
- Understand what language models are and their applications
- Learn the evolution from n-grams to neural language models
- Explore probability distributions over text sequences
- Visualize language model predictions and perplexity

## 📚 Theory

### What is a Language Model?
A language model assigns probabilities to sequences of words. Given a sequence of words w₁, w₂, ..., wₙ, the model computes:

**P(w₁, w₂, ..., wₙ) = P(w₁) × P(w₂|w₁) × P(w₃|w₁,w₂) × ... × P(wₙ|w₁,...,wₙ₋₁)**

### Types of Language Models

1. **N-gram Models**: Use fixed-context windows
   - Unigram: P(wᵢ)
   - Bigram: P(wᵢ|wᵢ₋₁)
   - Trigram: P(wᵢ|wᵢ₋₂,wᵢ₋₁)

2. **Neural Language Models**: Use neural networks to model context
   - RNN-based models
   - Transformer-based models (GPT, BERT)

3. **Applications**:
   - Text generation
   - Machine translation
   - Speech recognition
   - Autocomplete systems

### Key Metrics

**Perplexity**: Measures how well the model predicts a sample
```
Perplexity = exp(-1/N × Σ log P(wᵢ|context))
```
Lower perplexity = better model

## 🚀 Interactive Application

Run the application to:
- Compare n-gram models (unigram, bigram, trigram)
- Visualize probability distributions
- Calculate perplexity on sample texts
- Generate text using different models
- See real-time performance metrics

## 📊 Features

- **Process Visualization**: Step-by-step model training
- **Numerical Metrics**: Perplexity, accuracy, vocabulary size
- **Graphical Outputs**: Probability distributions, comparison charts
- **Interactive Controls**: Adjust n-gram order, temperature, sample size

## 🎮 Usage

```bash
python app.py
```

Then open http://localhost:8000 in your browser.

## 🧪 Exercises

1. Train models on different text corpora and compare perplexity
2. Implement add-k smoothing for n-gram models
3. Visualize how context length affects predictions
4. Generate text and analyze quality vs. n-gram order

## 📖 References

- Jurafsky & Martin, "Speech and Language Processing", Chapter 3
- Bengio et al., "A Neural Probabilistic Language Model" (2003)
- Shannon, "A Mathematical Theory of Communication" (1948)
