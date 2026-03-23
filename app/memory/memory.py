MAX_MEMORY = 10
conversation_memory = []
user_profile = {
    "name": None,
    "mood": None,
    "last_intent": None
}

def set_mood(mood: str):
    user_profile["mood"] = mood

def save_mood(mood: str):
    user_profile["mood"] = mood

def get_profile():
    return user_profile

def add_message(role: str, content: str):
    conversation_memory.append({
        "role": role,
        "content": content
    })

    if len(conversation_memory) > MAX_MEMORY:
        conversation_memory.pop(0)

def save_name(name: str):
    user_profile["name"] = name

def get_name():
    return user_profile.get("name")
    
def get_memory():
    return conversation_memory
