from random import sample

class Word(object):
    def __init__(self, english, language, translation, gender):
        self.english = english
        self.language = language
        self.translation = translation
        self.gender = gender

class WordSet(object):
    def __init__(self, language, topic, words):
        self.language = language
        self.topic = topic
        self.words = words

class Quiz(object):
    def __init__(self, aSet):
        self.set = aSet
        self.score = 0

    def randomise(self, length):
        return sample(range(length), len(range(length)))

    def quiz(self):
        deck = self.randomise(len(self.set.words))

        while True:
            try:
                index = deck.pop()
            except IndexError:
                self.score = float(self.score/2)
                highestPossibleScore = str(len(self.set.words))
                print("\nRound over! Your score that round was " + '%g'%(self.score) + " out of " + highestPossibleScore + ".\n")
                self.randomise(len(self.set.words))
                self.score = 0
                return
            textIn = input("What is the gender of '" + self.set.words[index].translation + "'? ").lower()
            if textIn == 'exit':
                return
            elif textIn == self.set.words[index].gender:
                print("Correct!")
                self.score += 1 # Half point, 1 so it's not adding floats
            else:
                print("Incorrect! The answer was " + self.set.words[index].gender + ".")
            textIn = ''
            textIn = input("What is that in English? ").lower()
            if textIn == "exit":
                return
            elif textIn == self.set.words[index].english:
                print("Correct!")
                self.score += 1 # Half point
            else:
                print("Incorrect! The answer was " + self.set.words[index].english + ".")
