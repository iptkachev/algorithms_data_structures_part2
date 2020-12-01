from typing import List
from hash_tables.hash_table import polynomial_hash


def search_substring(text: str, pattern: str, p: int = 1_000_000_007, x: int = 263) -> List[int]:
    """
    Алгоритм Рабина-Карпа для поиска подстроки в строке. Время О(|text| + число_вхождений * |pattern|)
    :param text: исходный текст
    :param pattern: substring для поиска
    :param p: простое число
    :param x: база многочлена, должно быть < p
    :return: индексы вхождений
    """
    hash_pattern = polynomial_hash(pattern, p, x, p)
    size_pattern = len(pattern)
    x_pow = pow(x, len(pattern) - 1, p)  # вычисляем заранее, чтобы сэкономить
    hash_window = polynomial_hash(text[-size_pattern:], p)
    hash_window_values = [hash_window]

    for i in range(len(text) - size_pattern - 1, -1, -1):
        # i - индекс добавляемого монома, i + size_pattern - индекс исключамеого монома
        hash_window = ((hash_window - ord(text[i + size_pattern]) * x_pow) * x % p + ord(text[i]) % p) % p
        hash_window_values.append(hash_window)

    count_windows = len(hash_window_values)
    substring_match_indices = []
    for i in range(count_windows):
        if hash_window_values[count_windows - i - 1] == hash_pattern:
            # доп. проверка из-за возможности коллизий
            if text[i: (i + size_pattern)] == pattern:
                substring_match_indices.append(i)

    return substring_match_indices


if __name__ == '__main__':
    assert search_substring('abraccghacc', 'acc') == [3, 8]
    assert search_substring('abraaaaghaaa', 'aaa') == [3, 4, 9]
    assert search_substring('testTesttesT', 'Test') == [4]
