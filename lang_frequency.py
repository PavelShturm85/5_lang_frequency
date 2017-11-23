import sys
import re
import collections


def load_data(enter_file):
    with open(enter_file, 'r') as text_file:
        return text_file.read()


def del_symbols(input_text):
    return re.sub('[^А-Яа-яA-Za-z\s]*', '', input_text.lower()).split()


def get_ten_top_words(words):
    top_ten = 10
    return collections.Counter(words).most_common(top_ten)


def print_top_words(top_ten):
    print('Самые встречающиеся слова:')
    print('---------------------------')
    for number, words_and_amount in enumerate((top_ten), 1):
        print("{} \t {} \t x {} ".format(number, *words_and_amount))


if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Введите путь к файлу: ')

    enter_text = load_data(input_file_name)
    top_ten_words = get_ten_top_words(del_symbols(enter_text))
    print_top_words(top_ten_words)
