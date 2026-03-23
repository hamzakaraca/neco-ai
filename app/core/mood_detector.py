from app.memory.memory import save_mood

MOOD_PATTERNS = {
    "yorgun": ["yoruldum", "çok yorgunum", "bitkinim"],
    "üzgün": ["moralim bozuk", "üzgünüm", "canım sıkkın"],
    "mutlu": ["çok mutluyum", "keyfim yerinde", "harika hissediyorum"]
}


def detect_mood(text: str):
    t = text.lower()

    for mood, patterns in MOOD_PATTERNS.items():
        for pattern in patterns:
            if pattern in t:
                save_mood(mood)
                return