# -*- coding: utf-8 -*-

from random import randint, shuffle

m,f,n,p = 'm','f','n','p'
germanWords = ['Realityshow', 'Musiksendung', 'Nachrichten', 'Quizsendung', 'Sportsendung',
         'Seifenoper', 'Castingshow', 'Documentarserie', 'Zeichentrickserie', 'Fernseher',
         'Dokumentarfilm', 'Fantasiefilm', 'Chatten', 'Handy', 'Telefon', 'Magazin',
         'Lied', 'Musikal', 'Dialoge', 'Filme', 'Sendungen', 'Liebesfilm',
         'Science-Fiction-Film', 'Zeichentrickfilm', 'Kassettenrekorder', 'Computer',
         'Laptop', 'Sänger', 'Schlagzeuger', 'Schauspieler', 'Stereoanlage',
         'Screibmaschine', 'Zeitung', 'Tageszeitung', 'Website',
         'Playstation (1, 2, 3, 4)', 'Xbox (360, One)', 'Mediathek', 'Videothek',
         'Onlinevideothek', 'Musik', 'Indiemusik', 'Rockmusik', 'Popmusik', 'Band',
         'Gruppe', 'Sängerin', 'Schlagzeugerin', 'Komödie', 'Geschichte',
         'Schauspielerin']

answer = [f, f, p, f, f, f, f, f, f, m, m, m, n, n, n, n, n, n, p, p, p, m, m, m,
          m, m, m, m, m, m, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f,
          f, f, f]

englishWords = ['reality show', 'music show', 'the news', 'quiz show', 'sports show',
                'soap opera', 'talent show', 'documentary series', 'cartoon series',
                'tv', 'documentary film', 'fantasy film', 'chat', 'mobile', 'phone',
                'magasine', 'song', 'musical', 'dialogue', 'films', 'shows', 'love film',
                'scifi film', 'cartoon film', 'cassette recorder', 'computer',
                'laptop', 'singer', 'drummer', 'actor', 'stereo', 'type writer',
                'newspaper', 'daily news', 'website', 'playstation', 'xbox',
                'media library', 'video library', 'streaming site', 'music', 'indie music',
                'rock music', 'pop music', 'band', 'group', 'singer', 'drummer',
                'comedy', 'story', 'actress']

# assert len(germanWords) == len(answer) == len(englishWords)

score = 0

deck = []
def randomise():
    global deck
    deck = list(range(1, len(germanWords)))
    shuffle(deck)
randomise()

running = True
while running:
    try:
        index = deck.pop()
    except IndexError:
        print("\n\nRound over! Your score that round was " + str(float(score)/2) + " out of " + str(float(len(answer))) + ".\n\n")
        randomise()
        score = 0
    textIn = input("What is the gender of '" + germanWords[index] + "'? ").lower()
    if textIn == 'exit':
        running = False
        break
    elif textIn == answer[index]:
        print("Correct!")
        score += 1 # Half mark, 1 so it's not adding floats
    else:
        print("Incorrect! The answer was " + answer[index] + ".")
    textIn = ''
    textIn = input("What is that in English? ").lower()
    if textIn == "exit":
        running = False
        break
    elif textIn == str(englishWords[index]):
        print("Correct!")
        score += 1 # Half point
    else:
        print("Incorrect! The answer was " + englishWords[index] + ".")
