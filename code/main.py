# -*- coding: utf-8 -*-

from random import randint, shuffle
import pickle
import os
import sys

import objects

# if __file__ == 'main.py':
words_filepath = 'words.p'

words = []

def load_words():
    global words
    try: # to load words
        with open(words_filepath, 'rb') as f:
            words = pickle.load(f)
    except FileNotFoundError: # Create file if not found
        print("Failed to find file '", words_filepath, "'.")
        with open(words_filepath, 'wb'):
            pass

def save_words():
    with open(words_filepath, 'wb') as output:
        pickle.dump(words, output, -1)

def check_word_exists(word, language=None):
    global words
    if language == 'english':
        for w in words:
            if w.english == word:
                return True
        return False
    elif language == 'german':
        for w in words:
            if w.german == word:
                return True
        return False
    elif language == 'french':
        for w in words:
            if w.french == word:
                return True
        return False
    else:
        for w in words:
            if w.english == word:
                return True
            if w.german == word:
                return True
            if w.french == word:
                return True
        return False

def add_word(english, german, french, germanGender, frenchGender):
    global words
    check_word_exists(english)
    words.append(objects.Word(english, german, french, germanGender, frenchGender))

score = 0

load_words()

def randomise(length):
    indexes = list(range(length))
    return shuffle(indexes)

deck = randomise(len(words))

running = True
while running:
    action = input("What would you like to do? ").lower()
    if action == 'add word':
        english = input("What is the word in English? ").lower()
        german = input("What is the word in German? ").lower()
        french = input("What is the word in French? ").lower()
        germanGender = input("What is the gender of that word in German? ").lower()
        frenchGender = input("What is the gender of that word in French? ").lower()

        add_word(english, german, french, germanGender, frenchGender)

    elif action == 'save words':
        save_words()

    elif action == 'exit':
        sys.exit()
    # try:
    #     index = deck.pop()
    # except IndexError:
    #     print("\n\nRound over! Your score that round was " + str(float(score)/2) + " out of " + str(float(len(answer))) + ".\n\n")
    #     randomise()
    #     score = 0
    # textIn = input("What is the gender of '" + germanWords[index] + "'? ").lower()
    # if textIn == 'exit':
    #     running = False
    #     break
    # elif textIn == answer[index]:
    #     print("Correct!")
    #     score += 1 # Half mark, 1 so it's not adding floats
    # else:
    #     print("Incorrect! The answer was " + answer[index] + ".")
    # textIn = ''
    # textIn = input("What is that in English? ").lower()
    # if textIn == "exit":
    #     running = False
    #     break
    # elif textIn == str(englishWords[index]):
    #     print("Correct!")
    #     score += 1 # Half point
    # else:
    #     print("Incorrect! The answer was " + englishWords[index] + ".")
