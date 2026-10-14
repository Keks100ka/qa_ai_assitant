import argparse
from testcase_generator import generate_testcases
from bug_report_formatter import format_bug_report
from history import get_last_records
from translator import translate_to_english


def main():
    """Разбирает аргументы и вызывает нужный сервис."""
    parser = argparse.ArgumentParser(
        description="AI-ассистент для QA-инженера"
    )

    # Подкоманды: testcase, bug, translate
    subparsers = parser.add_subparsers(dest="command")

    # Команда testcase
    testcase_parser = subparsers.add_parser("testcase", help="Сгенерировать тест-кейсы по описанию фичи")
    testcase_parser.add_argument("description", help="Описание фичи")

    # Команда bug
    bug_parser = subparsers.add_parser("bug", help="Оформить баг-репорт по сырому описанию")
    bug_parser.add_argument("description", help="Сырое описание бага")

    
    # Команда translate
    translate_parser = subparsers.add_parser("translate", help="Перевод текст на английский для QA")
    translate_parser.add_argument("text", help="Введите текст на русском")


    # Команда history
    history_pasrer = subparsers.add_parser("history", help="Вывести последние записи")
    history_pasrer.add_argument(
        "--N", 
        type=int, 
        default=10, 
        help="Сколько последних записей показать (по умолчанию - 10)"
    )

    # Разбираем аргументы
    args = parser.parse_args()

    # Выполняем нужную команду
    if args.command=="testcase":
        print("Генерирую тест-кейсы...\n")
        result = generate_testcases(args.description)
        print(result)

    elif args.command=="bug":
        print("Оформляю баг-репорт...\n")
        result = format_bug_report(args.description)
        print(result)

    elif args.command=="translate":
        print("Перевожу на английский...\n")
        result = translate_to_english(args.text)
        print(result)

    elif args.command=="history":
        records = get_last_records(args.N)
        if not records:
            print("История пуста.")
        else:
            for i, record in enumerate(records, 1):
                print(f"---Запись {i} ---")
                print(f"Время: {record['timestamp']}")
                print(f"Команда: {record['command']}")
                print(f"Запрос: {record['input']}")
                print(f"Ответ: {record['output'][200:]}...")
                print()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

