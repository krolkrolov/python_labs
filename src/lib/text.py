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