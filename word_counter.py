def read_file(filename):
    """Зчитує вміст файлу з вказаною назвою."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().lower()
