from app.memory.memory import get_memory, save_name,get_name
from app.core.rules import RULES

def extract_name(text: str):
    text = text.lower()

    if "adım" in text:
        parts = text.split("adım")
        if len(parts) > 1:
            return parts[1].strip().split()[0]

    return None



from app.memory.memory import get_memory, save_name, get_name

def run_rules(user_message: str):
    text = user_message.lower()

    # 1️⃣ İSİM HATIRLAMA (recall)
    if "adım" in text and ("neydi" in text or "hatırlıyor" in text):
        name = get_name()
        if name:
            return f"Adın {name}"
        else:
            return "Henüz adını bilmiyorum."

    # 2️⃣ İSİM KAYDETME (save)
    if "adım" in text and "?" not in text:
        parts = text.split()
        if len(parts) >= 2:
            name = parts[-1]
            save_name(name)
            return f"Memnun oldum {name}, adını hatırlayacağım."

    # 3️⃣ FALLBACK
    return None


