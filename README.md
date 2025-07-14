# MedMentor_AI + GenAI AgentOS Protocol

## 🧠 Introduction

**MedMentor.AI** is a multilingual AI-powered assistant designed to help patients understand complex medical diagnoses in simple terms. Built using the **GenAI AgentOS Protocol**, it combines modular AI agents into a seamless workflow that explains, translates, and generates downloadable health summaries.

## ⚙️ Agent Workflow

```
          +-------------------------+
          |   Patient Diagnosis     |
          |   (Text input)          |
          +-------------------------+
                       |
                       v
          +-------------------------+
          | medical_explainer_agent |
          | Explains diagnosis      |
          +-------------------------+
                       |
                       v
          +-----------------------------+
          | language_translator_agent   |
          | Translates to Hindi, Marathi, Spanish |
          +-----------------------------+
                       |
                       v
          +-------------------------+
          | care_summary_agent     |
          | Generates PDF summary  |
          +-------------------------+
```

## 🤖 Agents Used

* **medical\_explainer\_agent**: Converts medical jargon into easy-to-understand text.
* **language\_translator\_agent**: Translates the explanation into Hindi, Marathi, and Spanish using OpenAI.
* **care\_summary\_agent**: Creates a printable PDF report with multilingual support using ReportLab.

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone git@github.com:monstrouscry/MedMentor_AI-GenAI-AgentOS-Protocol.git
```

### 2. Navigate to CLI

```bash
cd genai-agentos/cli
```

### 3. Create virtual environment

```bash
python -m venv .venv
source .venv/Scripts/activate  # on Windows
```

### 4. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 5. Register agents

```bash
python cli.py register_agent -n "medical_explainer_agent" -d "Explains complex diagnoses"
python cli.py register_agent -n "language_translator_agent" -d "Translates to Hindi, Marathi, Spanish"
python cli.py register_agent -n "care_summary_agent" -d "Generates a PDF summary"
```

### 6. Run agents

```bash
uv run agents/medical_explainer_agent/medical_explainer_agent.py
uv run agents/language_translator_agent/language_translator_agent.py
uv run agents/care_summary_agent/care_summary_agent.py
```

## 📦 Tech Stack

* **GenAI AgentOS Protocol**
* **OpenAI GPT-4** for explanation + translation
* **ReportLab** for PDF generation
* **Python 3.10+**

## 🧪 Demo Video

> 🔗 https://youtu.be/XG62UBUgo00?si=A3ozydmzQ2xpy-in

## 📄 Notion Submission

> [📘 Notion Project Page](https://stream-nut-6a2.notion.site/MedMentor_AI-An-AI-AgentOS-Powered-Health-Literacy-Assistant-230134ce466280f0b1d2ec03dbdd4bfb?pvs=73)

## 🏆 Bonus Points Completed

* ✅ GenAI AgentOS Protocol Used (5 pts)
* ✅ Notion Submission (1 pt)

## 📎 Optional Assets

* [Slide Deck (12 slides)](assets/MedMentor_AI_PitchDeck.pdf)
* [PDF Report Sample](agents/care_summary_agent/patient_summary.pdf)

## 📜 License

This project is licensed under the MIT License.


- ✅ **Notion Documentation (1 point)**  
  The slide deck and supporting documentation were created and shared via Notion.  
  This satisfies the criteria for 1 bonus point as per hackathon guidelines.

https://www.notion.so/MedMentor_AI-An-AI-AgentOS-Powered-Health-Literacy-Assistant-230134ce466280f0b1d2ec03dbdd4bfb?source=copy_link
