"""
This program calculates ther reading level of a text using the Coleman-Liau index,
which usese the following formula:
index = 0.0588 * L - 0.296 * S - 15.8
L = average number of letters per 100 words in the text
S = average number of sentences per 100 words in the text
"""


def main():
    text = input('Text: ')
    letter_count = count_letters(text)
    word_count = count_words(text)
    sentence_count = count_sentences(text)
    index = calculate_index(letter_count, word_count, sentence_count)
    print_result(index)


def count_letters(text):
    alph = set('abcdefghijklmnopqrstuvwxyz')  # Use a set for O(1) access
    res = 0
    for ch in text:
        if ch.lower() in alph:
            res += 1
    return res


def count_words(text):
    res = 1
    for ch in text:
        if ch == ' ':
            res += 1
    return res


def count_sentences(text):
    terminators = set('.!?')  # Use a set for O(1) access
    res = 0
    for ch in text:
        if ch in terminators:
            res += 1
    return res


# This is based on the Coleman-Liau index
def calculate_index(letter_count, word_count, sentence_count):
    l = float(letter_count) / float(word_count) * 100
    s = float(sentence_count) / float(word_count) * 100
    index = 0.0588 * l - 0.296 * s - 15.8
    return round(index)


def print_result(index):
    if index < 1:
        print('Before Grade 1')
    elif index > 16:
        print('Grade 16+')
    else:
        print(f'Grade {index}')


main()