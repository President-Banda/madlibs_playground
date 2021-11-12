# Python 3.8
# Coding: UTF-8
import db.connector

my_test = "love_letter_three"


def get_words():
    name = (my_test,)
    types = db.connector.cursor
    sql = """SELECT `types` FROM `sentences` WHERE `name`=%s"""
    types.execute(sql, name)
    types = types.fetchall()
    word_dictionary = {}
    words = ""
    # print(types)
    for items in types:
        # print(items)
        for item in items:
            words = item.split(',')

    # print(words)

    for item in words:
        word_dictionary.update({item: []})

    return word_dictionary


def get_sentence(sentence_name):
    sentence_name = (sentence_name, )
    sentences = db.connector.cursor
    sql = """SELECT `sentence` FROM `sentences` WHERE `name`=%s"""
    sentences.execute(sql, sentence_name)
    sentence = sentences.fetchall()
    return sentence


def get_user_input(args):
    # Getting user input
    for types, word in args.items():
        args[types] = str(input("Please enter a/an {}: ".format(types)))

    return args


def clean_sentence(sentence):
    for item in sentence:
        for extra in item:
            return extra


def compile():
    sentence = get_sentence(my_test)
    sentence = str(clean_sentence(sentence)).strip()
    word = get_words()
    user_words = get_user_input(word)
    print(sentence.format(**user_words))


compile()
