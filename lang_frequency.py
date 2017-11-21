import sys
import re
import collections


def load_data(enter_file):
    with open(enter_file, 'r') as text_file:
        return text_file.read()


def del_symbols(input_text):
    return re.sub('[^А-Яа-яA-Za-z\s]*', '', input_text.lower()).split()


def print_top_words(words_dict):

    print('Самые встречающиеся слова:')
    print('---------------------------')
    top_ten = 10
    for number, words_and_amount in enumerate(
            collections.Counter(words_dict).most_common(top_ten), 1):
        print("{} \t {} \t x {} ".format(number, *words_and_amount))


if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Введите путь к файлу: ')

    enter_text = load_data(input_file_name)
    print_top_words(del_symbols(enter_text))
