import argparse
from testcase_generator import generate_testcases
from bug_report_formatter import format_bug_report


def main():
    """Разбирает аргументы и вызывает нужный сервис."""
    parser = argparse.ArgumentParser(
        description="AI-ассистент для QA-инженера"
    )

    # Подкоманды: testcase, bug, translate
    subparsers = parser.add_subparsers(dest="command")

    # Команда testcase
    testcase_parser = subparsers.add_parser(
        "testcase",
        help="Сгенерировать тест-кейсы по описанию фичи"
    )
    testcase_parser.add_argument(
        "description",
        help="Описание фичи"
    )

    # Команда bug
    bug_parser = subparsers.add_parser(
        "bug",
        help="Оформить баг-репорт по сырому описанию"
    )
    bug_parser.add_argument("description", help="Сырое описание бага")

    # Разбираем аргументы
    args = parser.parse_args()

    # Выполняем нужную команду
    if args.command == "testcase":
        print("Генерирую тест-кейсы...\n")
        result = generate_testcases(args.description)
        print(result)

    elif args.command == "bug":
        print("Оформляю баг-репорт...\n")
        result = format_bug_report(args.description)
        print(result)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

