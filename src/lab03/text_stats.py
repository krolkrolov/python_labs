import sys
import re
from collections import Counter
from typing import Dict, List, Tuple


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace('Ё', 'Е').replace('ё', 'е')
    
    if casefold:
        text = text.casefold()
    
    text = re.sub(r'[\t\r\n]', ' ', text)
    
    text = ''.join(char for char in text if char.isprintable() or char.isspace())
    
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def tokenize(text: str) -> List[str]:
    tokens = re.findall(r'\b[\w-]+\b', text)
    return tokens


def count_freq(tokens: List[str]) -> Dict[str, int]:
    return dict(Counter(tokens))


def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]




# from text import normalize, tokenize, count_freq, top_n

import io
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')


def main():
    text = sys.stdin.read().strip()
    
    if not text:
        print("Ошибка: ввод пустой")
        return
    
    clean_text = normalize(text)
    words = tokenize(clean_text)
    
    if not words:
        print("Ошибка: нет слов для анализа")
        return
    
    total = len(words)
    unique = len(set(words))
    freqs = count_freq(words)
    top_words = top_n(freqs, 5)
    
    print(f"Всего слов: {total}")
    print(f"Уникальных слов: {unique}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()