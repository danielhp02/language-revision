# -*- coding: utf-8 -*-

from random import sample

class Noun(object):
    def __init__(self, english, language, translation, gender):
        self.english = english
        self.language = language
        self.translation = translation
        self.gender = gender

class Verb(object):
    def __init__(self, english, language, translation, pastParticiple, auxVerb):
        self.english = english
        self.language = language
        self.translation = translation
        self.pastParticiple = pastParticiple
        self.auxVerb = auxVerb

class WordSet(object):
    def __init__(self, language, topic, nouns, verbs):
        self.language = language
        self.topic = topic
        self.nouns = nouns
        self.verbs = verbs

class Quiz(object):
    def __init__(self, coloured):
        self.score = 0
        self.coloured = coloured

    def randomise(self, length):
        return sample(range(length), len(range(length)))

    def nouns(self, aSet):
        deck = self.randomise(len(aSet.words))

        while True:
            try:
                index = deck.pop()
            except IndexError:
                self.score = float(self.score/2)
                highestPossibleScore = str(len(aSet.words))
                print(self.coloured("\nRound over! Your score that round was " + '%g'%(self.score) + " out of " + highestPossibleScore + ".\n", 'cyan'))
                self.score = 0
                return

            textIn = input(self.coloured("What is the gender of '" + aSet.words[index].translation + "'? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.words[index].gender:
                print(self.coloured("Correct!", 'green'))
                self.score += 1 # Half point, 1 so it's not adding floats
            else:
                print(self.coloured("Incorrect! The answer was " + aSet.words[index].gender + ".", 'red'))

            textIn = input(self.coloured("What is that in English? ", 'cyan', True)).lower()
            if textIn == "exit":
                return
            elif textIn == aSet.words[index].english:
                print(self.coloured("Correct!", 'green'))
                self.score += 1 # Half point
            else:
                print(self.coloured("Incorrect! The answer was " + aSet.words[index].english + "." + ".", 'red'))

    def verbs(self, aSet): # At the moment, this is for past prticiples. A conjugation quiz will be added soon
        deck = self.randomise(len(aSet.words))
        auxiliaryVerbs = [haben, sein] if aSet.language == 'german' else [avoir, être] # Not very flexible, I know. Will update.

        while True:
            try:
                index = deck.pop()
            except IndexError:
                self.score = float(self.score/2)
                highestPossibleScore = str(len(aSet.words))
                print(self.coloured("\nRound over! Your score that round was " + '%g'%(self.score) + " out of " + highestPossibleScore + ".\n", 'cyan'))
                self.score = 0
                return

            textIn = input(self.coloured("What is the past participle of '" + aSet.words[index].pastParticiple + "'? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.words[index].pastParticiple:
                print(self.coloured("Correct!", 'green'))
                self.score += 1 # Half point, 1 so it's not adding floats
            else:
                print(self.coloured("Incorrect! The answer was " + aSet.words[index].pastParticiple + ".", 'red'))

            textIn = input(self.coloured("Does '" + aSet.words[index].translation + "' use " + auxiliaryVerbs[0] + " or " + auxiliaryVerbs[1] +"? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.words[index].auxVerb:
                print(self.coloured("Correct!", 'green'))
                self.score += 1 # Half point, 1 so it's not adding floats
            else:
                print(self.coloured("Incorrect! The answer was " + aSet.words[index].auxVerb + ".", 'red'))

            textIn = input(self.coloured("What is the english translation of '" + aSet.words[index].translation + "'? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.words[index].english:
                print(self.coloured("Correct!", 'green'))
                self.score += 1 # Half point, 1 so it's not adding floats
            else:
                print(self.coloured("Incorrect! The answer was " + aSet.words[index].english + ".", 'red'))
