from groq import Groq

from app.config import get_groq_api_key

MODEL_ID = "openai/gpt-oss-120b"


# Create groq client
def create_groq_client() -> Groq:
    api_key = get_groq_api_key()

    client = Groq(api_key=api_key, timeout=15.0, max_retries=0)

    return client
