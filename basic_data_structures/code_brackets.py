from typing import Union


def check_brackets(string_brackets: str) -> Union[str, int]:
    """
    Возвращает 'Success' если все скобки закрывают, в противном случае первую незакрытую скобку
    :param string_brackets: строка из скобок
    :return: Union[str, int]
    """
    map_brackets = {']': '[', '}': '{', ')': '('}
    stack = []
    stack_indexes = []
    for i, bracket in enumerate(string_brackets):
        if bracket in map_brackets.values():
            stack.append(bracket)
            stack_indexes.append(i)
        elif bracket in map_brackets.keys():
            if not stack:
                return i + 1
            if map_brackets.get(bracket, False) == stack[-1]:
                stack.pop()
                stack_indexes.pop()
            else:
                return i + 1
    if not stack:
        return 'Success'
    return stack_indexes[-1] + 1


if __name__ == '__main__':
    assert check_brackets('([](){([])})') == 'Success'
    assert check_brackets('()[]}') == 5
    assert check_brackets('{{[()]]') == 7
    assert check_brackets('((({[]})') == 2
    assert check_brackets('{}([]') == 3
    assert check_brackets('(slkj, {lk[lve]}, l)') == 'Success'
    assert check_brackets('(slkj{lk[lsj]}') == 1
    assert check_brackets('dasdsadsadas]]]') == 13
