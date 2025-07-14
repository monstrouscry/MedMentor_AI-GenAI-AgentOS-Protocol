# MedMentor_AI + GenAI AgentOS Protocol

## 🔍 Overview
**MedMentor_AI** is a multi-agent health literacy assistant designed to explain medical diagnoses, translate them into regional languages, and summarize care instructions using distinct AI agents. Built on top of the **GenAI AgentOS Protocol**, this system orchestrates communication between agents seamlessly.

## 🎯 Challenge Statement
- Task: “Explain a medical diagnosis in Hindi and Kannada, summarize care plan, and generate a follow-up reminder schedule.”
- Agents involved:
  1. **Symptom Interpreter Agent** – parses physician text or medical report.
  2. **Translator Agent** – multi-language translation.
  3. **Care Summarizer Agent** – creates concise action plans.
  4. **Reminder Planner Agent** – outputs structured follow-up schedule json.

## 🧩 Architecture & Workflow

```plaintext
[Master Agent]
     ↓
[Symptom Interpreter Agent] ↔ [Medical Knowledge DB]
     ↓
[Translator Agent] → Hindi, Marathi, Spanish
     ↓
[Care Summarizer Agent]
     ↓
[Reminder Planner Agent]
