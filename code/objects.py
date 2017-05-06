class Word(object):
    def __init__(self, english, german, french, gGender, fGender):
        self.english = english
        self.german = german
        self.germanGender = gGender
        self.french = french
        self.frenchGender = fGender

m = 'm'
f = 'f'
n = 'n'
p = 'p'

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

germanGenders = [f, f, p, f, f, f, f, f, f, m, m, m, n, n, n, n, n, n, p, p, p, m, m, m,
              m, m, m, m, m, m, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f,
              f, f, f]

words = []
