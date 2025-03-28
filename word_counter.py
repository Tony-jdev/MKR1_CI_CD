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


def write_results(filename, word_counts):
    """Записує результати у файл у форматі слово-кількість."""
    with open(filename, 'w', encoding='utf-8') as file:
        for word, count in word_counts:
            file.write(f"{word}-{count}\n")


def process_file(input_filename, output_filename):
    """Обробляє файл і записує топ-10 слів у вихідний файл."""
    try:
        text = read_file(input_filename)
        words = extract_words(text)
        top_words = get_top_words(words)
        write_results(output_filename, top_words)
        print(f"Обробка завершена успішно! Результати записано у файл '{output_filename}'")
    except FileNotFoundError:
        print(f"Помилка: файл '{input_filename}' не знайдено.")
    except Exception as e:
        print(f"Виникла неочікувана помилка: {str(e)}")


if __name__ == "__main__":
    process_file("sample.txt", "top_words.txt")
