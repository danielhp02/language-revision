# -*- coding: utf-8 -*-

from random import randint
import json
import os
import sys
import readline

import objects, inout

# if __file__ == 'main.py':
words_filepath = '../database/words.json'

if len(sys.argv) > 1:
    if sys.argv[1] == 'v':
        quiet = False
    else:
        quiet = True
else:
    quiet = True

wordSets = []

def load_words():
    global wordSets

    try: # to load words
        with open(words_filepath, 'r') as wordsIn:
            sets_dict = json.load(wordsIn)["sets"]

        for ws in sets_dict:
            if not quiet:
                print(inout.coloured("Loading set of topic: " + ws['topic'], 'magenta'))
            noun_list = []
            if len(ws["nouns"]) > 0:
                if not quiet:
                    print(inout.coloured("Loading nouns of topic: " + ws['topic'], 'magenta'))
                for n in ws["nouns"]:
                    noun_list.append(add_noun(n["english"], n["language"], n['translation'], n["gender"], quiet=quiet))
            verb_list = []
            if len(ws["verbs"]) > 0:
                if not quiet:
                    print(inout.coloured("Loading verbs of topic: " + ws['topic'], 'magenta'))
                for v in ws["verbs"]:
                    verb_list.append(add_verb(v["english"], v["language"], v['translation'], v["pastParticiple"], v["auxVerb"], quiet=quiet))

            add_set(ws["language"], ws["topic"], noun_list, verb_list, True)
            if not quiet:
                print(inout.coloured(ws['topic'] + " successfully loaded.", 'magenta'))
    except FileNotFoundError: # Create file if not found
        if not quiet:
            print(inout.coloured("Failed to find file '" + words_filepath + "'.", 'yellow'))
        with open(words_filepath, 'w') as output:
            json.dump({}, output, -1, indent=2)
    except KeyError: # If there is nothing in objects
        print(inout.coloured("You need to add some words.\nDon't forget to save!", 'yellow'))

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
    print(inout.coloured("Words saved.", "magenta"))

def findSet(language, topic, quiet, createSet=True):
    found = None
    for s in wordSets:
        # print(s.topic)
        if s.topic == topic:
            found = s
            if not quiet:
                print(inout.coloured("Set found for topic '" + topic + "'.", 'magenta'))
            break
    else:
        if not quiet:
            print(inout.coloured("Set for topic '" + topic + "' not found.", 'magenta'))
        if createSet:
            add_set(language, topic, [], [])
            return wordSets[-1]
    return found

def findWord(aSet, english, quiet): # Need to update
    found = None
    for i, w in enumerate(aSet.words):
        if w.english == english:
            found = i
            if not quiet:
                print(inout.coloured("Word '" + english + "' found in set '" + topic + "'.", 'magenta'))
            break
    else:
        if not quiet:
            print(inout.coloured("Word '" + english + "' not found in set '" + topic + "'.", 'magenta'))
        return None
    return found

def add_noun(english, language, translation, gender, topic=None, quiet=False):
    if topic is not None:
        wSet = findSet(language, topic, quiet, False)
        if wSet is not None:
            wSet.nouns.append(objects.Noun(english, language, translation, gender))
            if not quiet:
                print(inout.coloured("Noun successfully added to set '" + topic + "'.", 'magenta'))
    else:
        if not quiet:
            print(inout.coloured("Noun successfully added.", 'magenta'))
        return objects.Noun(english, language, translation, gender)

def add_verb(english, language, translation, pastParticiple, auxVerb, topic=None, quiet=False):
    if topic is not None:
        wSet = findSet(language, topic, quiet)
        if wSet is not None:
            wSet.verbs.append(objects.Verb(english, language, translation, pastParticiple, auxVerb))
            if not quiet:
                print(inout.coloured("Verb successfully added to set '" + topic + "'.", 'magenta'))
    else:
        if not quiet:
            print(inout.coloured("Verb successfully added.", 'magenta'))
        return objects.Verb(english, language, translation, pastParticiple, auxVerb)

def add_set(language, topic, nouns, verbs, quiet=False):
    global wordSets
    wordSets.append(objects.WordSet(language, topic, nouns, verbs))
    if not quiet:
        print(inout.coloured("New topic "+topic+" created.", 'magenta'))

def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def print_words_in_set(language, topic):
    aSet = findSet(language, topic, quiet, False)
    if aSet is not None:
        print("Nouns:")
        for n in aSet.nouns:
            print(n.translation, '-', n.english)
        print("Verbs:")
        for v in aSet.verbs:
            print(v.translation, '-', v.english)

load_words()
quiz = objects.Quiz()

running = True
try:
    while running:
        action = input(inout.coloured("What would you like to do? ", 'blue', True)).lower()
        if len(action) > 0:
            if action == 'add word':
                english = input(inout.coloured("What is the word in English? ", 'magenta', True)).lower()
                language = input(inout.coloured("What language? ", 'magenta', True)).lower()
                translation = input(inout.coloured("What is the word in " + language + "? ", 'magenta', True)).lower()
                topic = input(inout.coloured("What topic is this word in? ", 'magenta', True)).lower()

                type = input(inout.coloured("What type of word is this? (noun/verb) ", 'magenta', True)).lower()
                if type == 'noun':
                    gender = input(inout.coloured("What is the gender of this noun? ", 'magenta', True)).lower()

                    add_noun(english, language, translation, gender, topic)
                elif type == 'verb':
                    pastParticiple = input(inout.coloured("What is the past participle of this verb? ", 'magenta', True)).lower()
                    auxVerb = input(inout.coloured("What auxiliary verb does this verb use? ", 'magenta', True)).lower()

                    add_verb(english, language, translation, pastParticiple, auxVerb, topic)

            elif action.split()[0] == 'quiz': # needs language, type and topic
                if len(action.split()) < 4:
                    print(inout.coloured("More info is needed to start a quiz.", 'yellow'))

                elif action.split()[1] == 'french':
                    if action.split()[2] == 'verbs':
                        quiz.verbs(findSet('french', action.split()[3].lower(), quiet))
                    elif action.split()[2] == 'nouns':
                        quiz.nouns(findSet('french', action.split()[3].lower(), quiet))

                elif action.split()[1] == 'german':
                    if action.split()[2] == 'verbs':
                        quiz.verbs(findSet('german', action.split()[3].lower(), quiet))
                    elif action.split()[2] == 'nouns':
                        quiz.nouns(findSet('german', action.split()[3].lower(), quiet))

            elif action.split()[0] == 'print': # language, topic
                print_words_in_set(action.split()[1], action.split()[2])

            elif action == 'save':
                save_words()

            elif action == 'exit':
                sys.exit()
except KeyboardInterrupt:
    print()
    sys.exit()
