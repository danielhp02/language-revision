# -*- coding: utf-8 -*-

from random import randint
import json
import os
import sys
import readline

import objects, inout

if len(sys.argv) > 1:
    if sys.argv[1] == '-v':
        quiet = False
    else:
        quiet = True
else:
    quiet = True

wordSets = []

# if __file__ == 'main.py':
words_filepath = '../database/words.json'

def load_words():
    global wordSets

    try: # to load words
        with open(words_filepath, 'r') as wordsIn:
            sets_dict = json.load(wordsIn)["sets"]

        for ws in sets_dict:
            if not quiet:
                print(inout.coloured("Loading set of topic: " + ws['topic'], 'magenta'))
            word_list = []
            if len(ws["words"]) > 0:
                if not quiet:
                    print(inout.coloured("Loading words of topic: " + ws['topic'], 'magenta'))
                for w in ws["words"]:
                    if w["type"] == "noun":
                        word_list.append(add_noun(w["english"], w["language"], w['translation'], w["gender"], quiet=quiet))
                    elif w["type"] == "verb":
                        word_list.append(add_verb(w["english"], w["language"], w['translation'], w["pastParticiple"], w["auxVerb"], quiet=quiet))
                    elif w["type"] == "adjective":
                        word_list.append(add_adjective(w["english"], w["language"], w['translation'], quiet=quiet))

            add_set(ws["language"], ws["topic"], word_list, True)
            if not quiet:
                print(inout.coloured(ws['topic'] + " successfully loaded.", 'magenta'))
    except FileNotFoundError: # Create file if not found
        if not quiet:
            print(inout.coloured("Failed to find file '" + words_filepath + "'.", 'yellow'))
        with open(words_filepath, 'w') as output:
            json.dump({}, output, -1, indent=2)
    except KeyError: # If there is nothing in words
        print(inout.coloured("You need to add some words.\nDon't forget to save!", 'yellow'))

def save_words():
    global wordSets

    jsonFormat = {"sets": []}
    for ws in wordSets:
        word_list = []
        for w in ws.words:
            word_list.append(w.__dict__)
        jsonFormat["sets"].append({"language": ws.language, "topic": ws.topic, "words": word_list})
    with open(words_filepath, 'w') as output:
        json.dump(jsonFormat, fp=output, indent=2)
    print(inout.coloured("Words saved.", "magenta"))

def findSet(topic, quiet, language=None, createSet=True):
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
        if createSet and language is not None:
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

def add_adjective(english, language, translation, topic=None, quiet=False):
    if topic is not None:
        wSet = findSet(topic, quiet, language)
        if wSet is not None:
            wSet.words.append(objects.Adjective(english, language, translation))
            if not quiet:
                print(inout.coloured("Adjective successfully added to set '" + topic + "'.", 'magenta'))
    else:
        if not quiet:
            print(inout.coloured("Adjective successfully added.", 'magenta'))
        return objects.Adjective(english, language, translation)

def add_noun(english, language, translation, gender, topic=None, quiet=False):
    if topic is not None:
        wSet = findSet(topic, quiet, language)
        if wSet is not None:
            wSet.words.append(objects.Noun(english, language, translation, gender))
            if not quiet:
                print(inout.coloured("Noun successfully added to set '" + topic + "'.", 'magenta'))
    else:
        if not quiet:
            print(inout.coloured("Noun successfully added.", 'magenta'))
        return objects.Noun(english, language, translation, gender)

def add_verb(english, language, translation, pastParticiple, auxVerb, topic=None, quiet=False):
    if topic is not None:
        wSet = findSet(topic, quiet, language)
        if wSet is not None:
            wSet.words.append(objects.Verb(english, language, translation, pastParticiple, auxVerb))
            if not quiet:
                print(inout.coloured("Verb successfully added to set '" + topic + "'.", 'magenta'))
    else:
        if not quiet:
            print(inout.coloured("Verb successfully added.", 'magenta'))
        return objects.Verb(english, language, translation, pastParticiple, auxVerb)

def add_set(language, topic, words, quiet=False):
    global wordSets
    wordSets.append(objects.WordSet(language, topic, words))
    if not quiet:
        print(inout.coloured("New topic "+topic+" created.", 'magenta'))

# def remove_duplicates(seq):
#     seen = set()
#     seen_add = seen.add
#     return [x for x in seq if not (x in seen or seen_add(x))]

def print_words_in_set(language, topic):
    aSet = findSet(topic, quiet, createSet=False)
    if aSet is not None:
        # print("Nouns:")
        # for n in aSet.nouns:
        #     print(n.translation, '-', n.english)
        print("Words:")
        for w in aSet.words:
            print(w.translation, '-', w.english)

def help(command=None):
    if command is None:
        print("Commands:")
        print(" - add word")
        print(" - quiz")
        print(" - print")
        print(" - help")
        print(" - save")
        print(" - exit")
        print("Enter help [command] to get info\non a specific command and its usage.")
    elif command == 'quiz':
        print("quiz")
        print("Usage: quiz [type] [topic] [length]")
        print("Description: Begin a quiz of type [type] and topic [topic].")
        print("Optional argument [length] specifies the number of questions asked.")
        print("Available types:")
        print(" - nouns")
        print(" - verbs (past participles)")
        print(" - vocab")
        print("Available topics:")
        print(" - Make your own! (see 'add word')")
    elif command == 'print':
        print("print")
        print("Usage: print [language] [topic]")
        print("Description: Prints out all the words in the specified language and topic.")
        print("Note: the language argument may be removed in a future version.")
        print("Available languanges:")
        print(" - French")
        print(" - German")
        print("Available topics:")
        print(" - Make your own! (see 'add word')")

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

                type = input(inout.coloured("What type of word is this? ", 'magenta', True)).lower()
                if type == 'noun':
                    gender = input(inout.coloured("What is the gender of this noun? ", 'magenta', True)).lower()
                    inout.remove_history_items(6)

                    add_noun(english, language, translation, gender, topic)
                elif type == 'verb':
                    pastParticiple = input(inout.coloured("What is the past participle of this verb? ", 'magenta', True)).lower()
                    auxVerb = input(inout.coloured("What auxiliary verb does this verb use? ", 'magenta', True)).lower()
                    inout.remove_history_items(7)

                    add_verb(english, language, translation, pastParticiple, auxVerb, topic)
                elif type == 'adjective':
                    inout.remove_history_items(5)

                    add_adjective(english, language, translation, topic)

            elif action.split()[0] == 'quiz': # needs type and topic and possible limit
                if len(action.split()) < 3:
                    print(inout.coloured("More info is needed to start a quiz.", 'yellow'))

                if len(action.split()) == 3:
                    if action.split()[1] == 'verbs':
                        quiz.verbs(findSet(action.split()[2], quiet))
                    elif action.split()[1] == 'nouns':
                        quiz.nouns(findSet(action.split()[2], quiet))
                    elif action.split()[1] == 'vocab':
                        quiz.vocab(findSet(action.split()[2], quiet))
                elif len(action.split()) == 4:
                    if action.split()[1] == 'verbs':
                        quiz.verbs(findSet(action.split()[2], quiet), action.split()[3])
                    elif action.split()[1] == 'nouns':
                        quiz.nouns(findSet(action.split()[2], quiet), action.split()[3])
                    elif action.split()[1] == 'vocab':
                        quiz.vocab(findSet(action.split()[2], quiet), action.split()[3])

            elif action.split()[0] == 'print': # language, topic
                print_words_in_set(action.split()[1], action.split()[2])

            elif action.split()[0] == 'help':
                if len(action.split()) == 2:
                    help(action.split()[1])
                else:
                    help()

            elif action == 'save':
                save_words()

            elif action == 'exit':
                sys.exit()
except KeyboardInterrupt:
    print()
    sys.exit()
