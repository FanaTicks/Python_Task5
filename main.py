import re

def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except Exception as e:
        return str(e)

def get_first_sentence(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return sentences[0] if sentences else None

def get_all_words(text):
    return re.findall(r'\w+', text)

def sort_words(words):
    ukr_words = [word for word in words if any(char in word for char in "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")]
    eng_words = [word for word in words if any(char in word for char in "abcdefghijklmnopqrstuvwxyz")]

    ukr_words_sorted = sorted(ukr_words, key=lambda word: word.lower())
    eng_words_sorted = sorted(eng_words, key=lambda word: word.lower())

    return ukr_words_sorted + eng_words_sorted

if __name__ == "__main__":
    file_path = input("Введіть шлях до файлу: ")
    text = read_file_content(file_path)

    if not text:
        print("Не можу прочитати файл або файл порожній!")
    else:
        first_sentence = get_first_sentence(text)
        print(f"Перше речення: {first_sentence}")

        words = get_all_words(text)
        sorted_words_list = sort_words(words)

        print(f"Відсортовані слова: {sorted_words_list}")
        print(f"Кількість слів: {len(words)}")
