# -*- coding: utf-8 -*-

from random import randint, sample
import json
import os
import sys

import objects

# if __file__ == 'main.py':
words_filepath = 'words.json'

words = []

def load_words():
    global words
    try: # to load words
        with open(words_filepath, 'r') as input:
            word_dict = json.load(input)["words"]
            for w in word_dict:
                word = add_word(w["english"], w["german"], w["french"], w["germanGender"], w["frenchGender"], w["catergories"])
    except FileNotFoundError: # Create file if not found
        print("Failed to find file '", words_filepath, "'.")
        with open(words_filepath, 'w'):
            json.dump({"words": []}, output, -1, indent=2)

def save_words():
    global words
    word_json = []
    for w in words:
        word_json.append(w.__dict__)
    with open(words_filepath, 'w') as output:
        json.dump({"words": word_json}, fp=output, indent=2)

def check_word_exists(word, language=None):
    global words
    if words != []:
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
    else:
        return False

def add_word(english, german, french, germanGender, frenchGender, catergories):
    global words
    # check_word_exists(english)
    words.append(objects.Word(english, german, french, germanGender, frenchGender, catergories))

score = 0

load_words()

def quiz():
    global score, words

    deck = randomise(len(words))

    while True:
        try:
            index = deck.pop()
        except IndexError:
            score = float(score/2)
            highestPossibleScore = str(len(words))
            print("\nRound over! Your score that round was " + '%g'%(score) + " out of " + highestPossibleScore + ".\n")
            randomise(len(words))
            score = 0
            return
        textIn = input("What is the gender of '" + words[index].german + "'? ").lower()
        if textIn == 'exit':
            return
        elif textIn == words[index].germanGender:
            print("Correct!")
            score += 1 # Half point, 1 so it's not adding floats
        else:
            print("Incorrect! The answer was " + words[index].germanGender + ".")
        textIn = ''
        textIn = input("What is that in English? ").lower()
        if textIn == "exit":
            return
        elif textIn == str(words[index].english):
            print("Correct!")
            score += 1 # Half point
        else:
            print("Incorrect! The answer was " + words[index].english + ".")

def randomise(length):
    return sample(range(length), 2)

running = True
while running:
    action = input("What would you like to do? ").lower()
    if action == 'add word':
        english = input("What is the word in English? ").lower()
        german = input("What is the word in German? ").lower()
        french = input("What is the word in French? ").lower()
        germanGender = input("What is the gender of that word in German? ").lower()
        frenchGender = input("What is the gender of that word in French? ").lower()
        catergories = input("What catergories are this word in? ").lower().split()

        add_word(english, german, french, germanGender, frenchGender, catergories)

    elif action == 'quiz me':
        quiz()

    elif action == 'save words':
        save_words()

    elif action == 'exit':
        sys.exit()
