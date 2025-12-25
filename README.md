# MinutesAI
MinutesAI is a simple Python project built to turn raw meeting transcripts into clear, structured meeting minutes.
The idea is straightforward: meetings generate a lot of unorganized text, and it’s often hard to extract key decisions and action items. MinutesAI is a starting point for solving that problem using AI and Large Language Models (LLMs).
Right now, the project focuses on reading and processing meeting transcripts, with plans to gradually evolve into an AI-powered meeting assistant.

## What this project does
Reads meeting transcripts from a text file

Acts as a base for AI-powered summarization

Keeps the code clean, simple, and easy to understand

Is designed to grow step-by-step rather than all at once

This project is intentionally minimal so it’s easy to learn from and extend.

## Project Structure
```
MinutesAI/
├── app.py                     # Main Python script
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files ignored by Git
├── samples/
│   └── sample_transcript.txt  # Example meeting transcript
└── README.md                  # Project documentation
```

## How to set it up
1️. Clone the repository
git clone https://github.com/ujjesha1312/minutes-ai-project.git
cd minutes-ai-project

2️. (Optional but recommended) Create a virtual environment
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows

3️. Install dependencies
pip install -r requirements.txt

--> Running the project
Once everything is set up, run:
python app.py
The script reads the transcript from:
samples/sample_transcript.txt
You can modify this file to test different meeting conversations.

### Sample transcript
The sample_transcript.txt file contains example meeting content so you can immediately see how the project works.
Feel free to edit it with your own meeting notes or discussion text.

### What’s coming next
This project is a work in progress. Planned improvements include:
AI-based meeting summarization
Automatic extraction of action items
Speaker-wise summaries
Integration with LLM APIs
Audio-to-text support for real meetings

Environment variables (planned)
Future versions will use environment variables for API keys, stored safely in a .env file:
OPENAI_API_KEY=your_api_key_here

### Contributions
This project is currently being developed as a learning and experimentation project.
Suggestions, improvements, and ideas are always welcome.
