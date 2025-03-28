import re

def read_file(filename):
    """Зчитує вміст файлу з вказаною назвою."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().lower()

def extract_words(text):
    """Розбиває текст на слова, ігноруючи пунктуацію."""
    return re.findall(r'\b\w+\b', text)