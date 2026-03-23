from app.memory.memory import add_message
from app.core.neco_engine import run_rules
from app.llm.llm_service import generate_ai_reply
from app.memory.memory import save_mood
from app.core.intent_detector import detect_intent, extract_name
from app.memory.memory import save_name
from app.core.command_parser import parse_command
import json

def detect_mood(text: str):
    t = text.lower()

    if "yoruldum" in t or "çok yorgunum" in t:
        save_mood("yorgun")
    elif "moralim bozuk" in t or "üzgünüm" in t:
        save_mood("üzgün")
    elif "çok mutluyum" in t or "keyfim yerinde" in t:
        save_mood("mutlu")

def generate_reply(user_message: str) -> str:

    add_message("user", user_message)

    detect_mood(user_message)

    command = parse_command(user_message)
    
    try:
        data = json.loads(command)
    except:
        data = {"intent": "CHAT"}

    intent = data.get("intent")

    if intent == "SAVE_NAME":

        name = data.get("name")

        if name:
            save_name(name)
            reply = f"Tamam, bundan sonra sana {name} diye hitap ederim 🙂"
            add_message("assistant", reply)
            return reply

    print("Intent:", intent)

    rule_reply = run_rules(user_message)
    if rule_reply:
        add_message("assistant", rule_reply)
        return rule_reply

    ai_reply = generate_ai_reply(user_message)
    add_message("assistant", ai_reply)
    return ai_reply