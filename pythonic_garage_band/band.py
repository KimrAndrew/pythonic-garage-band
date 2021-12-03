class Band():

    instances = []

    def __init__(self, name = None, members = []):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __eq__(self, other):
        return self.name == other.name and self.members == other.members
    def to_list(self):
        return self.members

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician():
    def __init__(self, name = None, instrument = None):
        self.name = name
        self.instrument = instrument
    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

class Guitarist(Musician):

    def __init__(self, name=None, instrument='guitar'):
        super().__init__(name=name, instrument=instrument)

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    def get_instrument(self):
        return self.instrument
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):

    def __init__(self, name=None, instrument='bass'):
        super().__init__(name=name, instrument=instrument)

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument
    def play_solo(self):
        return 'bom bom buh bom'

class Drummer(Musician):

    def __init__(self, name=None, instrument='drums'):
        super().__init__(name=name, instrument=instrument)


    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'


    def get_instrument(self):
        return self.instrument


    def play_solo(self):
        return 'rattle boom crash'
    