# -*- coding: utf-8 -*-
# NOTE: make loading less verbose, esp. with creating words and sets
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
            sets_dict = json.load(wordsIn)["sets"]

        for ws in sets_dict:
            print(coloured("Loading set of topic: " + ws['topic'], 'magenta'))
            noun_list = []
            if len(ws["nouns"]) > 0:
                print(coloured("Loading nouns of topic: " + ws['topic'], 'magenta'))
                for n in ws["nouns"]:
                    noun_list.append(add_noun(n["english"], n["language"], n['translation'], n["gender"]))
            verb_list = []
            if len(ws["verbs"]) > 0:
                print(coloured("Loading verbs of topic: " + ws['topic'], 'magenta'))
                for v in ws["verbs"]:
                    verb_list.append(add_verb(v["english"], v["language"], v['translation'], v["pastParticiple"], v["auxVerb"]))

            add_set(ws["language"], ws["topic"], noun_list, verb_list)
            print(coloured(ws['topic'] + " successfully loaded.", 'magenta'))
    except FileNotFoundError: # Create file if not found
        print(coloured("Failed to find file '" + words_filepath + "'.", 'yellow'))
        with open(words_filepath, 'w') as output:
            json.dump({}, output, -1, indent=2)
    except KeyError: # If there is nothing in objects
        print(coloured("You need to add some words.\nDon't forget to save!", 'yellow'))

def save_words():
    global wordSets

    jsonFormat = {"sets": []}
    for ws in wordSets:
        nouns = []
        verbs = []
        for w in ws.nouns:
            words.append(w.__dict__)
        for w in ws.verbs:
            verbs.append(w.__dict__)
        jsonFormat["sets"].append({"language": ws.language, "topic": ws.topic, "nouns": nouns, "verbs": verbs})
    with open(words_filepath, 'w') as output:
        json.dump(jsonFormat, fp=output, indent=2)
    print(coloured("Words saved.", "magenta"))

def findSet(language, topic, createSet=True):
    found = None
    for s in wordSets:
        # print(s.topic)
        if s.topic == topic:
            found = s
            print(coloured("Set found for topic '" + topic + "'.", 'magenta'))
            break
    else:
        print(coloured("Set for topic '" + topic + "' not found.", 'magenta'))
        if createSet:
            add_set(language, topic, [], [])
            return wordSets[-1]
    return found

def findWord(aSet, english): # Need to update
    found = None
    for i, w in enumerate(aSet.words):
        if w.english == english:
            found = i
            print(coloured("Word '" + english + "' found in set '" + topic + "'.", 'magenta'))
            break
    else:
        print(coloured("Word '" + english + "' not found in set '" + topic + "'.", 'magenta'))
        return None
    return found

def add_noun(english, language, translation, gender, topic=None):
    if topic is not None:
        wSet = findSet(language, topic, False)
        if wSet is not None:
            wSet.nouns.append(objects.Noun(english, language, translation, gender))
            print(coloured("Noun successfully added to set '" + topic + "'.", 'magenta'))
    else:
        print(coloured("Noun successfully added.", 'magenta'))
        return objects.Noun(english, language, translation, gender)

def add_verb(english, language, translation, pastParticiple, auxVerb, topic=None):
    if topic is not None:
        wSet = findSet(language, topic) # do if stuff
        wSet.verbs.append(objects.Verb(english, language, translation, pastParticiple, auxVerb))
        print(coloured("Verb successfully added to set '" + topic + "'.", 'magenta'))
    else:
        return objects.Verb(english, language, translation, pastParticiple, auxVerb)

def add_set(language, topic, nouns, verbs):
    global wordSets
    wordSets.append(objects.WordSet(language, topic, nouns, verbs))
    print(coloured("New topic "+topic+" created.", 'magenta'))

def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def print_words_in_set(language, topic):
    aSet = findSet(language, topic, False)
    if aSet is not None:
        print("Nouns:")
        for n in aSet.nouns:
            print(n.translation, '-', n.english)
            print("hey")
        print("Verbs:")
        for v in aSet.verbs:
            print(v.translation, '-', v.english)

def coloured(text, colour, bold=False):
    # Blue is main UI
    # Yellow is for warnings
    # Green/red for correct/incorrect answers
    # Cyan is for quizes
    # Magenta is word storage related
    reset = '\u001b[0m'
    if not bold: # Not bold will be info
        if colour == 'black':
            return '\u001b[30m' + text + reset
        elif colour == 'red':
            return '\u001b[31m' + text + reset
        elif colour == 'green':
            return '\u001b[32m' + text + reset
        elif colour == 'yellow':
            return '\u001b[33m' + text + reset
        elif colour == 'blue':
            return '\u001b[34m' + text + reset
        elif colour == 'magenta':
            return '\u001b[35m' + text + reset
        elif colour == 'cyan':
            return '\u001b[36m' + text + reset
        elif colour == 'white':
            return '\u001b[37m' + text + reset
    else: # Bold will be questions/require input
        if colour == 'black':
            return '\u001b[30;1m' + text + reset
        elif colour == 'red':
            return '\u001b[31;1m' + text + reset
        elif colour == 'green':
            return '\u001b[32;1m' + text + reset
        elif colour == 'yellow':
            return '\u001b[33;1m' + text + reset
        elif colour == 'blue':
            return '\u001b[34;1m' + text + reset
        elif colour == 'magenta':
            return '\u001b[35;1m' + text + reset
        elif colour == 'cyan':
            return '\u001b[36;1m' + text + reset
        elif colour == 'white':
            return '\u001b[37;1m' + text + reset

load_words()
quiz = objects.Quiz(coloured)

running = True
try:
    while running:
        action = input(coloured("What would you like to do? ", 'blue', True)).lower()
        if action == 'add word':
            english = input(coloured("What is the word in English? ", 'magenta', True)).lower()
            language = input(coloured("What language? ", 'magenta', True)).lower()
            translation = input(coloured("What is the word in " + language + "? ", 'magenta', True)).lower()
            topic = input(coloured("What topic is this word in? ", 'magenta', True)).lower()

            type = input(coloured("What type of word is this? (noun/verb) ", 'magenta', True)).lower()
            if type == 'noun':
                gender = input(coloured("What is the gender of this noun? ", 'magenta', True)).lower()

                add_noun(english, language, translation, gender, topic)
            elif type == 'verb':
                pastParticiple = input(coloured("What is the past participle of this verb? ", 'magenta', True)).lower()
                auxVerb = input(coloured("What auxiliary verb does this verb use? ", 'magenta', True)).lower()

                add_verb(english, language, translation, pastParticiple, auxVerb, topic)

        elif action.split()[0] == 'quiz': # needs language, type and topic
            if len(action.split()) in [1,2,3]:
                print(coloured("More info is needed to start a quiz.", 'yellow'))
            elif action.split()[1] == 'french':
                if action.split()[2] == 'verbs':
                    quiz.verbs(findSet('french', action.split()[3].lower()))
                elif action.split()[2] == 'nouns':
                    quiz.nouns(findSet('french', action.split()[3].lower()))
            elif action.split()[1] == 'german':
                if action.split()[2] == 'verbs':
                    quiz.verbs(findSet('german', action.split()[3].lower()))
                elif action.split()[2] == 'nouns':
                    quiz.nouns(findSet('german', action.split()[3].lower()))

        elif action.split()[0] == 'print':
            print_words_in_set(action.split()[1], action.split()[2])

        elif action == 'save':
            save_words()

        elif action == 'exit':
            sys.exit()
except KeyboardInterrupt:
    print()
    sys.exit()
