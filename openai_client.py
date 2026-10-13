import os
from dotenv import load_dotenv
from openai import OpenAI

# Загружаем переменные из .env в окружение (сделать строго ДО создания OpenAI)
load_dotenv()

# Явная проверка наличия ключа в системе
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Error: OPENAI_API_KEY in .env not found")

# Создаем единый экземпляр клиента для всего проекта
client = OpenAI()