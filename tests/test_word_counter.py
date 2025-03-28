import pytest
from word_counter import read_file, extract_words, get_top_words, write_results, process_file

@pytest.fixture
def sample_text():
    """Фікстура для тестового тексту."""
    return "це тест це приклад приклад текст"

@pytest.fixture
def temp_file(tmp_path):
    """Фікстура для створення тимчасового файлу."""
    file = tmp_path / "test.txt"
    file.write_text("це тест це приклад приклад текст", encoding='utf-8')
    return str(file)

def test_read_file(temp_file):
    """Тест зчитування файлу."""
    content = read_file(temp_file)
    assert content == "це тест це приклад приклад текст"

@pytest.mark.parametrize("text, expected", [
    ("це тест, приклад!", ["це", "тест", "приклад"]),
    ("Яблуко.Груша", ["Яблуко", "Груша"]),
    ("Ананас   диня...Гарбуз", ["Ананас", "диня", "Гарбуз"]),
    ("", []),
])
def test_extract_words(text, expected):
    """Тест вилучення слів з параметризацією."""
    result = extract_words(text)
    assert result == expected

def test_get_top_words(sample_text):
    """Тест отримання топ слів."""
    words = extract_words(sample_text)
    result = get_top_words(words, 3)
    assert result == [("це", 2), ("приклад", 2), ("тест", 1)]

def test_write_results(tmp_path):
    """Тест запису результатів у файл."""
    output_file = tmp_path / "output.txt"
    word_counts = [("це", 2), ("тест", 1)]
    write_results(str(output_file), word_counts)
    with open(output_file, 'r', encoding='utf-8') as f:
        assert f.read() == "це-2\nтест-1\n"

def test_process_file(temp_file, tmp_path):
    """Тест повного процесу обробки файлу."""
    output_file = tmp_path / "result.txt"
    process_file(temp_file, str(output_file))
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "це-2" in content
    assert "приклад-2" in content