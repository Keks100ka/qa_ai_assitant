from openai_client import client
from config import MODEL, SYSTEM_ROLE
from history import add_record


def format_bug_report(raw_description):

    prompt = (
        f"Оформи следующий баг в структурированный баг-репорт:\n\n"
        f"{raw_description}\n\n"
        f"Формат ответа\n"
        f"**Заголовок:** <краткое описание проблемы>\n"
        f"**Шаги для воспроизведения:**\n"
        f"1. ...\n"
        f"2. ...\n"
        f"**Ожидаемый результат:** <что должно происходить>\n"
        f"**Фактический результат:** <что происходит на самом деле>\n"
        f"**Приоритет:** <Critical / Major / Minor>\n"
        f"**Окружение:** <если можно предположить>\n\n"
        #f"Дай ответ в формате JSON, без лишних пояснений."
    )
    
    response = client.chat.completions.create(
       model= MODEL,
       messages=[
           {"role": "system", "content": SYSTEM_ROLE},
           {"role": "user", "content": prompt},       
       ],
       temperature=0
    )

    answer = response.choices[0].message.content
    
    add_record("bug", raw_description, answer)
    
    return answer