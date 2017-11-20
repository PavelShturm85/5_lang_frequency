import sys
import re
import collections


def load_data(enter_file):
    with open(enter_file, 'r') as text_file:
        return text_file.read()


def del_symbols(input_text):
    return re.sub(u'[^А-Яа-яA-Za-z\s]*', u'', input_text.lower()).split()


def counter_words(word_list):
    counter = collections.Counter()
    for word in word_list:
        counter[word] += 1
    return counter


def print_top_words(word_dict):

    print('Самые встречающиеся слова:')
    print('---------------------------')
    top_ten = 10
    for number, counted_words in enumerate(word_dict.most_common(top_ten), 1):
        word = counted_words[0]
        quantity = counted_words[1]
        print("{} \t {} \t x {} ".format(number, word, quantity))


if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_file_name = sys.argv[1]
    else:
        input_file_name = input('Введите путь к файлу: ')

    enter_text = load_data(input_file_name)
    most_often_words = counter_words(del_symbols(enter_text))
    print_top_words(most_often_words)
