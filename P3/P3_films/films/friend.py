class Friend:
    def __init__(self, name, film=None):
        self.name = name
        self.film = film

        if film:
            film.location = self

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
