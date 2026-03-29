from app.llm.llm_client import ask_llm
from app.memory.memory import get_memory, get_profile
from app.core.neco_persona import NECO_SYSTEM_PROMPT


def generate_ai_reply(user_message: str) -> str:
    memory = get_memory()
    profile = get_profile()

    messages = [
        {"role": "system", "content": NECO_SYSTEM_PROMPT}
    ]

    context_parts = []

    if profile.get("name"):
        context_parts.append(f"Kullanıcının adı {profile['name']}.")

    if profile.get("mood"):
        context_parts.append(f"Kullanıcının şu anki ruh hali {profile['mood']}.")

    if context_parts:
        messages.append({
            "role": "system",
            "content": " ".join(context_parts)
        })

    for msg in memory:
        messages.append(msg)

    messages.append({
        "role": "user",
        "content": user_message
    })

    return ask_llm(messages)