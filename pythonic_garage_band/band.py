class Band():
    pass

class Musician():
    pass

class Guitarist():
    def __init__(self, name = None):
        self.name = name
    def __str__(self):
        return 'My name is Joan Jett and I play guitar'

    def __repr__(self):
        return 'Guitarist instance. Name = Joan Jett'
class Bassist():
    pass

class Drummer():
    def __init__(self, name = None):
        self.name = name
    def __str__(self):
        return 'My name is Sheila E. and I play drums'