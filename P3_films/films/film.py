class Film:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

class FilmVHF(Film):
    type = "vhf"
    def __init__(self, name, date):
        super().__init__(name, date)
        self.magnetic_tape = True

class FilmDVD(Film):
    type = "dvd"

    def __init__(self, name, date):
        super().__init__(name, date)
        self.mega_octets = 4700