import re
from collections import Counter
from typing import Dict, List, Tuple


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""

    if yo2e:
        text = text.replace("Ё", "Е").replace("ё", "е")

    if casefold:
        text = text.casefold()

    # Заменяем все пробельные символы на обычные пробелы
    text = re.sub(r"[\t\r\n]", " ", text)

    # Удаляем непечатаемые символы и заменяем их на пробелы
    text = "".join(char if char.isprintable() else " " for char in text)

    # Заменяем множественные пробелы на один и убираем пробелы по краям
    text = re.sub(r"\s+", " ", text).strip()

    return text


def tokenize(text: str) -> List[str]:
    if not text:
        return []

    # Используем улучшенное регулярное выражение для токенизации
    tokens = re.findall(r"\b[\w-]+\b", text)
    return tokens


def count_freq(tokens: List[str]) -> Dict[str, int]:
    if not tokens:
        return {}

    return dict(Counter(tokens))


def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    if not freq or n <= 0:
        return []

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]

# count_freq + top_n
freq = count_freq(["a", "b", "a", "c", "b", "a"])
assert freq == {"a": 3, "b": 2, "c": 1}
assert top_n(freq, 2) == [("a", 3), ("b", 2)]

# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]
