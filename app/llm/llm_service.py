from app.llm.llm_client import ask_llm
from app.memory.memory import get_memory, get_profile
from app.core.neco_persona import NECO_SYSTEM_PROMPT


def generate_ai_reply(user_message: str) -> str:
    memory = get_memory()
    profile = get_profile()

    messages = [
        {
            "role": "system",
            "content": NECO_SYSTEM_PROMPT
        }
    ]

    # 👇 YUMUŞAK MEMORY INJECTION
    if profile:
        memory_context = ", ".join(
            f"{k}: {v}" for k, v in profile.items()
        )

        messages.append({
            "role": "system",
            "content": f"Konuşma sırasında fark ettiğin şeyler: {memory_context}"
        })

    # 👇 GERÇEK KONUŞMA
    for msg in memory:
        messages.append(msg)

    messages.append({
        "role": "user",
        "content": user_message
    })

    return ask_llm(messages)
