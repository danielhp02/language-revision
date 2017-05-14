from random import sample

class Word(object):
    def __init__(self, english, german, french, gGender, fGender, catergories):
        self.english = english
        self.german = german
        self.germanGender = gGender
        self.french = french
        self.frenchGender = fGender

        self.catergories = catergories

class Quiz(object):
    def __init__(self, words):
        self.words = words
        self.score = 0

    def randomise(self, length):
        return sample(range(length), 2)

    def quiz(self, language):
        genderLanguage = 'germanGender' if language == 'german' else 'frenchGender'
        deck = self.randomise(len(self.words))

        while True:
            try:
                index = deck.pop()
            except IndexError:
                self.score = float(self.score/2)
                highestPossibleScore = str(len(self.words))
                print("\nRound over! Your score that round was " + '%g'%(self.score) + " out of " + highestPossibleScore + ".\n")
                self.randomise(len(self.words))
                self.score = 0
                return
            textIn = input("What is the gender of '" + getattr(self.words[index], language) + "'? ").lower()
            if textIn == 'exit':
                return
            elif textIn == getattr(self.words[index], genderLanguage):
                print("Correct!")
                self.score += 1 # Half point, 1 so it's not adding floats
            else:
                print("Incorrect! The answer was " + getattr(self.words[index], genderLanguage) + ".")
            textIn = ''
            textIn = input("What is that in English? ").lower()
            if textIn == "exit":
                return
            elif textIn == getattr(self.words[index], 'english'):
                print("Correct!")
                self.score += 1 # Half point
            else:
                print("Incorrect! The answer was " + getattr(self.words[index], 'english') + ".")
