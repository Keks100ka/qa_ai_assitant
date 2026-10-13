import argparse
from testcase_generator import generate_testcases

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

    # Разбираем аргументы
    args = parser.parse_args()

    # Выполняем нужную команду
    if args.command == "testcase":
        print("Генерирую тест-кейсы...\n")
        result = generate_testcases(args.description)
        print(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

