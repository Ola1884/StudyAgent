# 🧠 StudyAgent: An Adaptive AI Planner for Students & Professionals

> **"Your personal AI study coach that plans, adapts, and learns from your progress."**

StudyAgent helps you manage lectures, assignments, and exams by generating realistic, dynamic study plans — and **replanning automatically when life gets in the way**. Built with agentic AI, NLP, and user-centered design.

## 🎯 Problem
Students often:
- Overestimate daily capacity → burnout
- Cram before exams due to poor planning
- Lack feedback when falling behind

Existing tools (Google Calendar, Todoist) are **passive** — they don’t *reason* or *adapt*.

## 💡 Solution
StudyAgent is an **agentic AI system** that:
1. **Understands** your goals via natural language or syllabus PDF
2. **Plans** a feasible schedule using spaced repetition + workload balancing
3. **Adapts** in real-time when you miss a session
4. **Forecasts** risk of missing deadlines

## 🛠️ Tech Stack
- **Core AI**: Llama 3 (7B) via Ollama + custom ReAct agent
- **NLP**: spaCy + fine-tuned instruction parsing
- **PDF Ingestion**: `marker` → Markdown → LLM extraction
- **Backend**: FastAPI + SQLite
- **Frontend**: Streamlit
- **Deployment**: Docker + Render
- **MLOps**: Weights & Biases (logging), GitHub Actions (CI)

## 📦 Features
- ✅ Natural language input: _“I’ve done 4/10 CV lectures, exam in 12 days”_
- ✅ Auto-ingest syllabus PDFs
- ✅ Daily adaptive replanning
- ✅ Progress tracking & deadline forecasting
- ✅ Voice input (Whisper) + TTS output (optional)

## 🚀 Quick Start
to be added
