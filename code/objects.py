# -*- coding: utf-8 -*-

from random import sample
import inout

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
    def __init__(self):
        self.score = 0

    def randomise(self, length):
        return sample(range(length), len(range(length)))

    def nouns(self, aSet): # NOTE: add new features from verb quiz to noun quiz
        deck = self.randomise(len(aSet.nouns))

        while True:
            try:
                index = deck.pop()
            except IndexError:
                self.score = float(self.score/2)
                highestPossibleScore = str(len(aSet.nouns))
                print(inout.coloured("\nRound over! Your score that round was " + '%g'%(self.score) + " out of " + highestPossibleScore + ".\n", 'cyan'))
                self.score = 0
                return

            textIn = input(inout.coloured("What is the gender of '" + aSet.nouns[index].translation + "'? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.nouns[index].gender:
                print(inout.coloured("Correct!", 'green'))
                self.score += 1 # Half point, 1 so it's not adding floats
            else:
                print(inout.coloured("Incorrect! The answer was " + aSet.nouns[index].gender + ".", 'red'))

            textIn = input(inout.coloured("What is that in English? ", 'cyan', True)).lower()
            if textIn == "exit":
                return
            elif textIn == aSet.nouns[index].english:
                print(inout.coloured("Correct!", 'green'))
                self.score += 1 # Half point
            else:
                print(inout.coloured("Incorrect! The answer was " + aSet.nouns[index].english + "." + ".", 'red'))

    def verbs(self, aSet): # At the moment, this is for past prticiples. A conjugation quiz will be added soon
        deck = self.randomise(len(aSet.verbs))
        numberOfQuestions = len(deck)
        auxiliaryVerbs = ['haben', 'sein'] if aSet.language == 'german' else ['avoir', 'etre'] # Not very flexible, I know. Will update. 'ê' is intentionally left out.

        while True:
            try:
                index = deck.pop()
            except IndexError:
                self.score = float(self.score/3) # 3 is the number of quesions for each verb
                highestPossibleScore = str(len(aSet.verbs))
                if self.score < 10:
                    print(inout.coloured("Round over! Your score that round was " + '%.2g'%(self.score) + " out of " + highestPossibleScore + ", " +'%0.4g'%(self.score/int(highestPossibleScore)*100) + "%.\n", 'cyan'))
                elif self.score < 100:
                    print(inout.coloured("Round over! Your score that round was " + '%.3g'%(self.score) + " out of " + highestPossibleScore + ", " +'%0.4g'%(self.score/int(highestPossibleScore)*100) + "%.\n", 'cyan'))
                elif self.score < 1000:
                    print(inout.coloured("Round over! Your score that round was " + '%.4g'%(self.score) + " out of " + highestPossibleScore + ", " +'%0.4g'%(self.score/int(highestPossibleScore)*100) + "%.\n", 'cyan'))
                self.score = 0
                return

            print(inout.coloured("Question " + str(numberOfQuestions - len(deck)) + ":", 'cyan'))
            textIn = input(inout.coloured("a) What is the past participle of '" + aSet.verbs[index].translation + "'? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.verbs[index].pastParticiple:
                print(inout.coloured("Correct!", 'green'))
                self.score += 1 # 1 to avoid adding floats
            else:
                print(inout.coloured("Incorrect! The answer was " + aSet.verbs[index].pastParticiple + ".", 'red'))

            textIn = input(inout.coloured("b) Does '" + aSet.verbs[index].pastParticiple + "' use " + auxiliaryVerbs[0] + " or " + auxiliaryVerbs[1] +"? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.verbs[index].auxVerb:
                print(inout.coloured("Correct!", 'green'))
                self.score += 1
            else:
                print(inout.coloured("Incorrect! The answer was " + aSet.verbs[index].auxVerb + ".", 'red'))

            textIn = input(inout.coloured("c) What is the english translation of '" + aSet.verbs[index].translation + "'? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.verbs[index].english:
                print(inout.coloured("Correct!", 'green'))
                self.score += 1
            else:
                print(inout.coloured("Incorrect! The answer was " + aSet.verbs[index].english + ".", 'red'))

            print()
