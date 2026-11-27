from app.ai.groq_provider import MODEL_ID, create_groq_client


# =====================================
# 1. GENERATE CHAT RESPONSE
# =====================================
def generate_chat_response(user_message: str):

    if not user_message.strip():
        raise ValueError("The user message cannot be empty.")

    # System instructions
    system_message = {
        "role": "system",
        "content": (
            "You are a helpful assistant specializing "
            "in League of Legends esports. "
            "Give concise and factual explanations. "
            "Do not invent current match results, "
            "roster changes, schedules, or quotations. "
            "If current information cannot be verified, "
            "say so."
        ),
    }

    # User's actual question
    user_message_data = {"role": "user", "content": user_message}

    # Combine the messages
    messages = [system_message, user_message_data]

    # Create the Groq client
    with create_groq_client() as client:
        completion = client.chat.completions.create(
            model=MODEL_ID,
            messages=messages,
            max_completion_tokens=256,
            reasoning_effort="low",
            include_reasoning=False,
            stream=False,
        )

    # Retrieve the assistant's response
    answer = completion.choices[0].message.content

    if not answer or not answer.strip():
        raise RuntimeError("The model returned no text response.")

    # Retrieve token usage
    usage = completion.usage

    return {
        "model": MODEL_ID,
        "content": answer.strip(),
        "usage": {
            "input_tokens": usage.prompt_tokens if usage else None,
            "output_tokens": usage.completion_tokens if usage else None,
            "total_tokens": usage.total_tokens if usage else None,
        },
    }
