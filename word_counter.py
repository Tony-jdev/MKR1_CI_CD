from collections import Counter
import re

def read_file(filename):
    """Зчитує вміст файлу з вказаною назвою."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().lower()

def extract_words(text):
    """Розбиває текст на слова, ігноруючи пунктуацію."""
    return re.findall(r'\b\w+\b', text)

def get_top_words(words, top_n=10):
    """Повертає top_n найпопулярніших слів."""
    return Counter(words).most_common(top_n)