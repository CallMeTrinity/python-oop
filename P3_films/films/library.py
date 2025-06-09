import random
from pprint import pprint

from .data import films
from .film_cleaner import FilmCleaner

class Library:
    def __init__(self):
        self.films = []
        for film_data in films:
            film = FilmCleaner(film_data).clean()
            film.location = self
            self.films.append(film)
        self.sort_by_name_and_date()

    def sort_by_name_and_date(self):
        self.films.sort(key=lambda film: film.date)
        self.films.sort(key=lambda film: film.name)

    def sort_by_type(self):
        self.films.sort(key=lambda film:film.type)

    def get_random_film(self):
        return self.films[random.randint(0, len(self.films) - 1)]

    def get_by_name(self, name):
        for film in self.films:
            if film.name == name:
                return film
        return None

    def get_films_lent(self):
        films_lent = []
        for film in self.films:
            if film.location is not self:
                films_lent.append(film)
        return films_lent