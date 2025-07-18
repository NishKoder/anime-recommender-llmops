import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

GROQ_MODEL_ID = os.getenv("GROQ_MODEL_ID")
if not GROQ_MODEL_ID:
    raise ValueError("GROQ_MODEL_ID environment variable is not set.")
