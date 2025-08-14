# for paths, model choices and etc
# User preferences and defaults
# Output formatting options

API_KEY = "AIzaSyAXI8qL-j1rB-6nUlbNNn5w724ka_pZFpE"
PATH = r"C:\Users\sheha\Desktop\مكتبتي\Chip Huyen - AI Engineering-O'Reilly Media, Inc. (2024).pdf"

START_PAGE = 21

LOCAL_MODEL = 'llama3.2'

PROMPT_TEMPLATE = """
You are an assistant that creates educational datasets.
Given the following text, generate:
1. A clear and concise question about the content.
2. A correct answer to that question.
3. A detailed explanation of why that answer is correct.

Text:
{text}

Respond ONLY in Valid JSON format as:
{{
    "question": "...",
    "answer": "...",
    "explanation": "..."
}}
"""

CHUNK_SIZE = 600
CHUNK_OVERLAP = 50

COOLDOWN = True
COOLDOWN_ITERATIONS = 100
COOLDOWN_TIME = 10