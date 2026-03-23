import re


def detect_intent(message: str) -> str:

    message = message.lower()

    if re.search(r"adım\s+\w+", message):
        return "SAVE_NAME"

    return "CHAT"


def extract_name(message: str):

    match = re.search(r"adım\s+(\w+)", message.lower())

    if match:
        return match.group(1)

    return None