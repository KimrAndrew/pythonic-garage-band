class Band():
    def __init__(self, name = None, members = []):
        self.name = name
        self.members = members

class Musician():
    def __init__(self, name = None):
        pass

class Guitarist(Musician):
    def __init__(self, name = ''):
        self.name = name
        super().__init__()
    def __str__(self):
        return 'My name is Joan Jett and I play guitar'

    def __repr__(self):
        return 'Guitarist instance. Name = Joan Jett'
    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def __init__(self, name = None):
        self.name = name
        super().__init__()

    def __str__(self):
        return 'My name is Meshell Ndegeocello and I play bass'

    def __repr__(self):
        return 'Bassist instance. Name = Meshell Ndegeocello'

    def get_instrument(self):
        return 'bass'
    def play_solo(self):
        return 'bom bom buh bom'

class Drummer(Musician):
    def __init__(self, name = None):
        self.name = name
        super().__init__()

    def __str__(self):
        return 'My name is Sheila E. and I play drums'


    def __repr__(self):
        return 'Drummer instance. Name = Sheila E.'


    def get_instrument(self):
        return 'drums'


    def play_solo(self):
        return 'rattle boom crash'
    