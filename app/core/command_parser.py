from app.llm.llm_client import ask_llm

def parse_command(message: str):

    prompt = f"""
Aşağıdaki kullanıcı mesajını analiz et.

Eğer bir komutsa:
intent ve gerekli verileri JSON olarak ver.

Eğer komut değilse:
intent = CHAT yaz.

Sadece JSON dön.

Örnekler:

Mesaj: "Adım Hamza"
Cevap:
{{"intent": "SAVE_NAME", "name": "Hamza"}}

Mesaj: "Bana Hamza diye hitap et"
Cevap:
{{"intent": "SAVE_NAME", "name": "Hamza"}}

Mesaj: "Nasılsın"
Cevap:
{{"intent": "CHAT"}}

---

Mesaj: "{message}"
"""

    response = ask_llm([
        {"role": "user", "content": prompt}
    ])

    return response