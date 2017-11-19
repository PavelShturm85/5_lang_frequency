import sys
import re
import string
import collections


def load_data(enter_file):
    with open(enter_file, 'r') as text:
        content = text.read()
    return content


def special_characters(input_text):
    regexp = ''.format(string.printable)
    return re.sub(regexp, '', input_text)


def get_most_frequent_words(without_special_symbol):
    counter = collections.Counter()
    for word in without_special_symbol.split():
        counter[word] += 1
    return counter


def print_top_words(word_dict):
    print('Самые встречающиеся слова:')
    print('---------------------------')
    place_counter = 1
    for i in word_dict.most_common(10):
        print(str(place_counter) + '.' + '\t', i[0], '\t x', i[1])
        place_counter += 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Введите путь к файлу: ')
    enter_text = load_data(input_file_name)
    most_often_words = get_most_frequent_words(special_characters(enter_text))
    print_top_words(most_often_words)
