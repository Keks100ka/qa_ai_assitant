# QA AI Assistant

AI-ассистент для QA-инженера. Помогает генерировать тест-кейсы, оформлять баг-репорты и переводить тексты на английский с помощью ChatGPT.

## Возможности

- **testcase** — генерация тест-кейсов по описанию фичи
- **bug** — оформление баг-репорта по сырому описанию
- **translate** — перевод текстов на английский в стиле QA
- **history** — просмотр последних запросов

## Требования

- Python 3.10+
- API-ключ OpenAI

## Установка

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/Keks100ka/qa_ai_assitant.git
   cd qa_ai_assistant

2. Создать виртуальное окружение и активировать:
    ```bash
    python -m venv venv
    venv\Scripts\activate    # Windows
    source venv/bin/activate # Linux/macOS

3. Установить зависимости:
    ```bash
    pip install -r requirements.txt

4. Создать файл .env и добавить ключ:
    ```bash
    OPENAI_API_KEY=sk-...

## Использовани

- Генерация тест-кейсов
    ```bash
    python main.py testcase "Логин с email и паролем"

- Оформление баг-репорта
    ```bash
    python main.py bug "кнопка войти не реагирует на клик"

- Перевод на английский
    ```bash
    python main.py translate "Пользователь не может войти после сброса пароля"

- Просмотр истории запроса-ответа
    ```bash
    python main.py history
    python main.py history --limit 5

## Структура проекта

qa_ai_assistant/
├── main.py                    # точка входа, разбор аргументов
├── config.py                  # настройки (модель, роли, пути)
├── openai_client.py           # клиент OpenAI
├── testcase_generator.py      # генератор тест-кейсов
├── bug_report_formatter.py    # оформление баг-репортов
├── translator.py              # перевод текстов
├── history.py                 # сохранение истории
├── data/
│   └── history.json           # файл истории
├── .env                       # ключ (не в репозитории)
├── .gitignore
├── requirements.txt
└── README.md

## Технологии

- Python 3
- OpenAI API (GPT-4o-mini)
- python-dotenv
- argparse

## Лицензия