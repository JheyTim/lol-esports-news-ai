from groq import APIConnectionError, APIStatusError, AuthenticationError, RateLimitError

from app.ai.groq_provider import MODEL_ID, create_groq_client


# Test groq connection
def check_groq_connection():
    try:
        # Initialize the groq client
        with create_groq_client() as client:
            # Retrieve available models
            models = client.models.list()

            # Extract model identifiers
            available_models = {model.id for model in models.data}

            print("Successfully connected to Groq API!")

            # Check whether our selected model is listed
            if MODEL_ID in available_models:
                print("GPT-OSS 120B is listed as available.")

            else:
                print("Connection successful.")
                print("Selected model was not found in the model list.")

    except AuthenticationError:
        print("Authentication failed (401).")
        print("Check whether your API key is valid.")

    except RateLimitError:
        print("Rate limit reached (429).")
        print("Stop and check your account limits.")

    except APIConnectionError:
        print("Unable to connect to Groq.")
        print("Check your internet connection.")

    except APIStatusError as error:
        print(f"Groq returned HTTP {error.status_code}.")

    except RuntimeError as error:
        print(error)


# Run coonection test

if __name__ == "__main__":
    check_groq_connection()
