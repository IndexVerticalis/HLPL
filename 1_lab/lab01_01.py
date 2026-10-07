import sys
import re

def word_freq(filename):
    counts = {}

    with open(filename, encoding='utf-8') as f:
        for line in f:
            for word in re.findall(r'\w+', line.lower()):
                counts[word] = counts.get(word, 0) + 1

    for word, count in counts.items():
        print(f"{word}: {count}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Неверный ввод - укажите путь к файлу")
    else:
        word_freq(sys.argv[1])

