# 🚀 Quick Start Guide

## Getting Started with 100 LLM Courses

### Prerequisites

```bash
# Install required Python packages
pip install numpy pandas matplotlib plotly torch transformers scikit-learn
```

### Launch the Course Catalog

1. **Open the main catalog:**
   ```bash
   # Simply open index.html in your browser
   # Or use Python's built-in server:
   python -m http.server 8000
   ```
   Then navigate to: http://localhost:8000

2. **Browse courses** by module or search for specific topics

3. **Launch any course** by clicking the "🚀 Launch Course" button

### Running Individual Courses

Each course has its own standalone application:

```bash
# Navigate to any course folder
cd course_001_introduction_to_language_models

# Run the course application
python app.py
```

The course will automatically open in your browser at http://localhost:8000

### Course Structure

Each course folder contains:
```
course_XXX_name/
├── app.py              # Python backend with API endpoints
├── index.html          # Interactive web interface
├── styles.css          # Modern styling
├── script.js           # Frontend logic and visualizations
└── README.md           # Course-specific documentation
```

### Features in Every Course

✅ **Process Visualization** - Watch algorithms work step-by-step  
✅ **Real-time Metrics** - See performance numbers update live  
✅ **Interactive Charts** - Explore data with Plotly visualizations  
✅ **Parameter Controls** - Adjust settings and see immediate results  
✅ **Responsive Design** - Works on desktop, tablet, and mobile  

### Learning Paths

#### 🌱 Beginner Path (Start Here!)
1. Course 001: Introduction to Language Models
2. Course 002: Tokenization Fundamentals
3. Course 007: RNN Fundamentals
4. Course 010: Attention Mechanism Basics
5. Course 031: Transformer Architecture

#### 🌿 Intermediate Path
1. Course 031: Transformer Architecture
2. Course 032: Self-Attention Mechanism
3. Course 041: Language Modeling Objectives
4. Course 045: BERT Pre-training
5. Course 051: Transfer Learning Basics
6. Course 055: LoRA

#### 🌳 Advanced Path
1. Course 061: RLHF
2. Course 064: RAG
3. Course 067: LLM Agents
4. Course 071: Model Quantization
5. Course 091: Mixture of Experts
6. Course 098: Interpretability

### Tips & Tricks

**Progress Tracking:**
- Double-click any course card to mark it as completed ✅
- Your progress is saved automatically in browser storage
- Call `exportProgress()` in browser console to download your progress

**Keyboard Shortcuts:**
- `Ctrl/Cmd + K` - Focus search box
- `Escape` - Clear search
- Module headers are clickable to collapse/expand

**Customization:**
- Each course can run independently
- Modify parameters in real-time
- Export results and visualizations

### Module Overview

| Module | Focus Area | Courses | Difficulty |
|--------|-----------|---------|------------|
| 1 | Foundations | 001-010 | 🟢 Beginner |
| 2 | Text Processing | 011-020 | 🟢 Beginner |
| 3 | Neural Networks | 021-030 | 🟡 Intermediate |
| 4 | Transformers | 031-040 | 🟡 Intermediate |
| 5 | Pre-training | 041-050 | 🟡 Intermediate |
| 6 | Fine-tuning | 051-060 | 🟡 Intermediate |
| 7 | Advanced Methods | 061-070 | 🔴 Advanced |
| 8 | Optimization | 071-080 | 🔴 Advanced |
| 9 | Applications | 081-090 | 🟡 Intermediate |
| 10 | Research Frontiers | 091-100 | 🔴 Advanced |

### Troubleshooting

**Port already in use:**
```bash
# Use a different port
python app.py --port 8001
# Or manually in app.py, change PORT = 8000 to PORT = 8001
```

**Missing dependencies:**
```bash
# Install all at once
pip install -r requirements.txt
```

**Browser doesn't open automatically:**
- Manually navigate to http://localhost:8000
- Check firewall settings
- Try a different browser

### Next Steps

1. ✅ Start with Module 1 if you're new to LLMs
2. ✅ Jump to specific topics if you have background knowledge
3. ✅ Complete exercises in each course
4. ✅ Build your own projects using learned concepts
5. ✅ Share your progress and insights!

### Support & Resources

- 📖 Each course has detailed README with theory
- 💻 All code is well-commented and modular
- 🎯 Exercises included for hands-on practice
- 📚 References to papers and additional resources

---

**Ready to become an LLM expert? Start your journey now! 🚀**
