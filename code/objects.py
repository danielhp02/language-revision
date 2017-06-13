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
        deck = self.randomise(len(aSet.nouns))

        while True:
            try:
                index = deck.pop()
            except IndexError:
                self.score = float(self.score/2)
                highestPossibleScore = str(len(aSet.nouns))
                print(self.coloured("\nRound over! Your score that round was " + '%g'%(self.score) + " out of " + highestPossibleScore + ".\n", 'cyan'))
                self.score = 0
                return

            textIn = input(self.coloured("What is the gender of '" + aSet.nouns[index].translation + "'? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.nouns[index].gender:
                print(self.coloured("Correct!", 'green'))
                self.score += 1 # Half point, 1 so it's not adding floats
            else:
                print(self.coloured("Incorrect! The answer was " + aSet.nouns[index].gender + ".", 'red'))

            textIn = input(self.coloured("What is that in English? ", 'cyan', True)).lower()
            if textIn == "exit":
                return
            elif textIn == aSet.nouns[index].english:
                print(self.coloured("Correct!", 'green'))
                self.score += 1 # Half point
            else:
                print(self.coloured("Incorrect! The answer was " + aSet.nouns[index].english + "." + ".", 'red'))

    def verbs(self, aSet): # At the moment, this is for past prticiples. A conjugation quiz will be added soon
        deck = self.randomise(len(aSet.verbs))
        auxiliaryVerbs = ['haben', 'sein'] if aSet.language == 'german' else ['avoir', 'etre'] # Not very flexible, I know. Will update. 'ê' is intentionally left out.

        while True:
            try:
                index = deck.pop()
            except IndexError:
                self.score = float(self.score/3) # 3 is the number of quesions for each verb
                highestPossibleScore = str(len(aSet.verbs))
                if self.score < 10:
                    print(self.coloured("Round over! Your score that round was " + '%.2g'%(self.score) + " out of " + highestPossibleScore + ", " +'%0.4g'%(self.score/int(highestPossibleScore)*100) + "%.\n", 'cyan'))
                elif self.score < 100:
                    print(self.coloured("Round over! Your score that round was " + '%.3g'%(self.score) + " out of " + highestPossibleScore + ", " +'%0.4g'%(self.score/int(highestPossibleScore)*100) + "%.\n", 'cyan'))
                elif self.score < 1000:
                    print(self.coloured("Round over! Your score that round was " + '%.4g'%(self.score) + " out of " + highestPossibleScore + ", " +'%0.4g'%(self.score/int(highestPossibleScore)*100) + "%.\n", 'cyan'))
                self.score = 0
                return

            textIn = input(self.coloured("What is the past participle of '" + aSet.verbs[index].translation + "'? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.verbs[index].pastParticiple:
                print(self.coloured("Correct!", 'green'))
                self.score += 1 # 1 to avoid adding floats
            else:
                print(self.coloured("Incorrect! The answer was " + aSet.verbs[index].pastParticiple + ".", 'red'))

            textIn = input(self.coloured("Does '" + aSet.verbs[index].pastParticiple + "' use " + auxiliaryVerbs[0] + " or " + auxiliaryVerbs[1] +"? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.verbs[index].auxVerb:
                print(self.coloured("Correct!", 'green'))
                self.score += 1
            else:
                print(self.coloured("Incorrect! The answer was " + aSet.verbs[index].auxVerb + ".", 'red'))

            textIn = input(self.coloured("What is the english translation of '" + aSet.verbs[index].translation + "'? ", 'cyan', True)).lower()
            if textIn == 'exit':
                return
            elif textIn == aSet.verbs[index].english:
                print(self.coloured("Correct!", 'green'))
                self.score += 1
            else:
                print(self.coloured("Incorrect! The answer was " + aSet.verbs[index].english + ".", 'red'))

            print()
