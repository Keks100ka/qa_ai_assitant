from openai_client import client
from config import MODEL, SYSTEM_ROLE


def generate_testcases(feature_description):

    promt = (
        f"Опиши тест-кейс для следующей фичи:\n\n"
        f"{feature_description}\n\n"
        f"Формат ответа\n\n"
        f"1. <название тест-кейса> - <что проверяем>\n"
        f"2. <название тест-кейса> - <что проверяем>\n"
        f"...\n\n"
        f"Дай 5-10 кейсов, покрывающих позитивные и негативные сценарии."
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_ROLE},
            {"role": "user", "content": promt}
        ],
        temperature=0         
    )

    return response.choices[0].message.content