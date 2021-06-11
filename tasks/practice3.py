from typing import List, Dict, Any


def filter_list(numbers: List[int]) -> List[int]:
    """
    Используя генератор списков (list comprehension) напишите код,
    который отфильтровывает все четные числа в списке.
    И возвращает результат фильтрации.

    На вход:
    - numbers - список состоящий из чисел

    На выходе:
    список только из нечетных чисел
    """

    # впишите ваш код здесь
    #return []
    return [a for a in numbers if a % 2 != 0]


def get_popular_category(operations: List[Dict[str, Any]]) -> str:
    """
    Функция анализирует список трат клиента по различным категориям товаров
    и находит категорию, в которой человек совершил больше всего покупок.

    На вход:
    - operations - список словарей в формате [{'category': 'название категории', 'amount': 100}]

    На выходе:
    строка - название категории в которой клиент совершил наибольшее количество покупок.
    """

    # впишите ваш код здесь
    # return max()
    max_a = 0
    for subject in operations:
        if subject['amount'] > max_a:
            max_c = subject['category']
            max_a = subject['amount']
    print(max_c)
    return max_c


def hide_personal_info(info: Dict[str, Any]) -> Dict[str, Any]:
    """
    Функция принимает на вход словарь содержащий информацию о клиенте.
    В словаре могут быть персональные данные клиента: ключи passport_code и phone_number.
    Если поля присутствуют - нужно защитить эти данные от злоумышленников.
    Для этого заменим все цифры в значениях этих полей на символ *.

    На вход:
    - info - словарь содержащий персональные данные клиента

    На выходе:
    - словарь в котором все персональные данные из описания функции - скрыты по алгоритму выше.
    """

    # впишите ваш код здесь
    for key, value in info.items():
        if key is 'passport_code':
            info[key] = info[key].replace("0", "*").replace("1", "*").replace("2", "*").replace("3", "*").replace("4", "*").replace("5", "*").replace("6", "*").replace("7", "*").replace("8", "*").replace("9", "*")
        if key is 'phone_number':
            info[key] = info[key].replace("0", "*").replace("1", "*").replace("2", "*").replace("3", "*").replace("4", "*").replace("5", "*").replace("6", "*").replace("7", "*").replace("8", "*").replace("9", "*")
    return info
    #return info


def main() -> None:
    pass


if __name__ == '__main__':
    main()
