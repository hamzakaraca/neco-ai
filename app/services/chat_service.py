import json
import re

from app.memory.memory import add_message, save_mood, save_name
from app.core.neco_engine import run_rules
from app.llm.llm_service import generate_ai_reply
from app.core.command_parser import parse_command
from app.core.mood_detector import detect_mood

def generate_reply(user_message: str) -> str:

    add_message("user", user_message)

    detect_mood(user_message)

   
    rule_reply = run_rules(user_message)
    if rule_reply:
        add_message("assistant", rule_reply)
        return rule_reply

    
    command = parse_command(user_message)

    match = re.search(r"\{.*\}", command, re.DOTALL)

    if match:
        try:
            data = json.loads(match.group())
        except:
            data = {"intent": "CHAT"}
    else:
        data = {"intent": "CHAT"}

    intent = data.get("intent")

   
    if intent == "SAVE_NAME":
        name = data.get("name")

        if name:
            save_name(name)
            reply = f"Tamam, bundan sonra sana {name} diye hitap ederim 🙂"
            add_message("assistant", reply)
            return reply

    
    ai_reply = generate_ai_reply(user_message)
    add_message("assistant", ai_reply)
    return ai_reply