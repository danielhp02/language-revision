class Word(object):
    def __init__(self, english, german, french, gGender, fGender, catergory):
        self.english = english
        self.german = german
        self.germanGender = gGender
        self.french = french
        self.frenchGender = fGender

        self.catergory = catergory

class Quiz(object):
    def __init__(self):
        pass

    def ask(self, catergory, task):
        pass
