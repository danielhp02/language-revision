# -*- coding: utf-8 -*-

from random import randint
import json
import os
import sys

import objects

# if __file__ == 'main.py':
words_filepath = 'words.json'

wordSets = []

def load_words():
    global wordSets
    try: # to load words
        with open(words_filepath, 'r') as wordsIn:
            word_dict = json.load(wordsIn)["sets"]
            for ws in word_dict:
                word_list = []
                for w in ws["words"]:
                    word_list.append(add_word(w["english"], w["language"], w['translation'], w["gender"]))
                add_set(ws["language"], ws["topic"], word_list)
    except FileNotFoundError: # Create file if not found
        print("Failed to find file '" + words_filepath + "'.")
        with open(words_filepath, 'w') as output:
            json.dump({}, output, -1, indent=2)
    except KeyError: # If there is nothing in objects
        print("You need to add some words and don't forget to save!")

def save_words():
    global wordSets

    jsonFormat = {"sets": []}
    for ws in wordSets:
        print("hey")
        words = []
        for w in ws.words:
            words.append(w.__dict__)
            print("ayy")
        jsonFormat["sets"].append({"language": ws.language, "topic": ws.topic, "words": words})
    with open(words_filepath, 'w') as output:
        json.dump(jsonFormat, fp=output, indent=2)

def findSet(language, topic):
    found = None
    for s in wordSets:
        print(s.topic)
        if s.topic == topic:
            found = s
            break
    else:
        add_set(language, topic, [])
        print("nah")
        return wordSets[-1]
    return found

def findWord(aSet, english):
    found = None
    for i, w in enumerate(aSet.words):
        if w.english == english:
            found = i
            break
    else:
        return None
    return found

def add_word(english, language, translation, gender, topic=None):
    if topic is not None:
        wSet = findSet(language, topic)
        wSet.words.append(objects.Word(english, language, translation, gender))
    else:
        return objects.Word(english, language, translation, gender)

def add_set(language, topic, words):
    global wordSets
    wordSets.append(objects.WordSet(language, topic, words))

def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def print_words_in_set(aSet):
    for w in aSet.words:
        print(w.english, '-', w.translation)

load_words()

running = True
while running:
    action = input("What would you like to do? ").lower()
    if action == 'add word':
        english = input("What is the word in English? ").lower()
        language = input("What language? ").lower()
        translation = input("What is the word in", language + "? ").lower()
        gender = input("What is the gender of that word? ").lower()
        topic = input("What topic is this word in? ").lower()

        add_word(english, language, translation, gender, topic)

    elif action.split()[0] == 'quiz': # needs language and topic
        print("eh")
        if len(action.split()) in [1,2]:
            print("More info is needed to start a quiz.")
        elif action.split()[1] == 'french':
            quiz = objects.Quiz(findSet('french', action.split()[2].lower()))
            quiz.quiz()
        elif action.split()[1] == 'german':
            quiz = objects.Quiz(findSet('german', action.split()[2].lower()))
            quiz.quiz()

    elif action == 'save':
        save_words()

    elif action == 'exit':
        sys.exit()
