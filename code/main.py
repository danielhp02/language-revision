# -*- coding: utf-8 -*-

from random import randint
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

def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

load_words()

catergories = []
for c in words:
    catergories.append(c.catergories)
catergories = remove_duplicates([y for x in catergories for y in x])

quiz = objects.Quiz(words)

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

    elif action.split()[0] == 'quiz':
        print("eh")
        if len(action.split()) in [1,2]:
            print("More info is needed to start a quiz.")
        elif action.split()[1] == 'french' and action.split()[2] in catergories:
            print('eh')
            quiz.quiz('french')
        elif action.split()[1] == 'german' and action.split()[2] in catergories:
            quiz.quiz('german')

    elif action == 'save words':
        save_words()

    elif action == 'exit':
        sys.exit()
