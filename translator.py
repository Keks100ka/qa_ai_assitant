from openai_client import client
from config import MODEL, SYSTEM_ROLE
from history import add_record

def translate_to_english(text):

    prompt = (
        f"Переведи следующий текст на английский язык.\n\n"
        f"Текст:\n"
        f"{text}\n\n"
        f"Требования к переводу: \n"
        f"- Используй техническую лексику, принятую в QA и разработке.\n"
        f"- Используй стиль как в баг-репортах и тикетах Jira.\n"
        f"- Не добавляй пояснений, только перевод\n"
        f"- Сохрани смысл, не сокращай."
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_ROLE},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    answer = response.choices[0].message.content

    add_record("translate", text, answer)

    return answer