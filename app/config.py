import os
from pathlib import Path

from dotenv import load_dotenv

# Project Location

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ENV_FILE = PROJECT_ROOT / ".env"

# Load enviroment variables
load_dotenv(dotenv_path=ENV_FILE, override=False)


# Get groq api key
def get_groq_api_key() -> str:
    api_key = os.getenv("GROQ_API_KEY", "").strip()

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is missing. Check your project-root .env file."
        )

    return api_key


# Check api key configuration
def is_groq_api_key_configured() -> bool:

    return bool(os.getenv("GROQ_API_KEY", "").strip())
