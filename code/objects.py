# -*- coding: utf-8 -*-

from random import sample
import sys
import inout
import readline

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

class Question(object):
    def __init__(self, record_history, colour):
        self.record_history = record_history
        self.colour = colour

    def eraseFromMemory(self):
        inout.remove_history_items(1)

    def ask(self, textIn):
        textIn = input(inout.coloured(textIn + ' ', self.colour, True)).lower()
        if self.record_history is False: self.eraseFromMemory()
        return textIn

class Quiz(object):
    def __init__(self):
        self.score = 0
        self.exit = False

    def randomise(self, length):
        return sample(range(length), len(range(length)))

    def displayScore(self, divisor, length):
        self.score /= divisor
        highestPossibleScore = str(length)
        if self.score < 10:
            print(inout.coloured("Round over! Your score that round was " + '%.2g'%(self.score) + " out of " + highestPossibleScore + ", " +'%0.4g'%(self.score/int(highestPossibleScore)*100) + "%.\n", 'cyan'))
        elif self.score < 100:
            print(inout.coloured("Round over! Your score that round was " + '%.3g'%(self.score) + " out of " + highestPossibleScore + ", " +'%0.4g'%(self.score/int(highestPossibleScore)*100) + "%.\n", 'cyan'))
        elif self.score < 1000:
            print(inout.coloured("Round over! Your score that round was " + '%.4g'%(self.score) + " out of " + highestPossibleScore + ", " +'%0.4g'%(self.score/int(highestPossibleScore)*100) + "%.\n", 'cyan'))
        self.score = 0

    def displayQuestionLetter(self, letter):
        print(inout.coloured("{})".format(letter), "cyan"), end=' ')

    def translationQuestion(self, word, letter=None):
        if self.exit is False:
            if letter is not None: self.displayQuestionLetter(letter)
            textIn = input(inout.coloured("What is {} in English? ".format(word.translation), 'cyan', True)).lower()
            if textIn == "exit":
                self.exit = True
            elif textIn == word.english:
                print(inout.coloured("Correct!", 'green'))
                self.score += 1
            else:
                print(inout.coloured("Incorrect! The answer was " + word.english + "." + ".", 'red'))
            inout.remove_history_items(1)

    def genderQuestion(self, noun, letter=None):
        if self.exit is False:
            if letter is not None: self.displayQuestionLetter(letter)
            textIn = input(inout.coloured("What is the gender of '" + noun.translation + "'? ", 'cyan', True)).lower()
            if textIn == 'exit':
                self.exit = True
            elif textIn == noun.gender:
                print(inout.coloured("Correct!", 'green'))
                self.score += 1
            else:
                print(inout.coloured("Incorrect! The answer was " + noun.gender + ".", 'red'))
            inout.remove_history_items(1)

    def pastParticipleQuestion(self, verb, letter=None):
        if self.exit is False:
            if letter is not None: self.displayQuestionLetter(letter)
            textIn = input(inout.coloured("What is the past participle of '" + verb.translation + "'? ", 'cyan', True)).lower()
            if textIn == 'exit':
                self.exit = True
            elif textIn == verb.pastParticiple:
                print(inout.coloured("Correct!", 'green'))
                self.score += 1
            else:
                print(inout.coloured("Incorrect! The answer was " + verb.pastParticiple + ".", 'red'))
            inout.remove_history_items(1)

    def auxiliaryVerbQuestion(self, verb, letter=None):
        auxiliaryVerbs = ['haben', 'sein'] if verb.language == 'german' else ['avoir', 'être'] # Shift-AltGr-6 release e for ê
        if self.exit is False:
            if letter is not None: self.displayQuestionLetter(letter)
            textIn = input(inout.coloured("Does '" + verb.pastParticiple + "' use " + auxiliaryVerbs[0] + " or " + auxiliaryVerbs[1] +"? ", 'cyan', True)).lower()
            if textIn == 'exit':
                self.exit = True
            elif textIn == verb.auxVerb:
                print(inout.coloured("Correct!", 'green'))
                self.score += 1
            else:
                print(inout.coloured("Incorrect! The answer was " + verb.auxVerb + ".", 'red'))
            inout.remove_history_items(1)

    def nouns(self, aSet):
        deck = self.randomise(len(aSet.nouns))
        numberOfQuestions = len(deck)

        while self.exit is False:
            try:
                index = deck.pop()
                questionNumber = numberOfQuestions - len(deck)
            except IndexError:
                self.displayScore(2, len(aSet.nouns))
                return

            print(inout.coloured("Question " + str(questionNumber) + ":", 'cyan'))
            self.translationQuestion(aSet.nouns[index], 'a')

            self.genderQuestion(aSet.nouns[index], 'b')

            print()

        self.exit = False

    def verbs(self, aSet): # At the moment, this is for past prticiples. A conjugation quiz will be added soon
        deck = self.randomise(len(aSet.verbs))
        numberOfQuestions = len(deck)

        while self.exit is False:
            try:
                index = deck.pop()
                questionNumber = numberOfQuestions - len(deck)
            except IndexError:
                self.displayScore(3, len(aSet.verbs))
                return

            print(inout.coloured("Question " + str(questionNumber) + ":", 'cyan'))
            self.pastParticipleQuestion(aSet.verbs[index], 'a')

            self.auxiliaryVerbQuestion(aSet.verbs[index], 'b')

            self.translationQuestion(aSet.verbs[index], 'c')

            print()

        self.exit = False
