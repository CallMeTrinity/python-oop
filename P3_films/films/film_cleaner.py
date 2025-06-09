from P3_films.films.film import FilmDVD, FilmVHF

class FilmCleaner:
    def __init__(self, film):
        self.film = film

    def clean(self):
        name = self.generate_name()
        date = self.generate_date()
        type = self.generate_type()

        for Film in (FilmVHF, FilmDVD):
            if type == Film.type:
                return Film(name, date)
            return None

    def generate_name(self):
        name_date = self.film[0]
        return name_date[: name_date.index("(")].strip()

    def generate_date(self):
        name_date = self.film[0]
        date_with_parenthesis = name_date[name_date.index("(") :]
        date = date_with_parenthesis.replace("(", "").replace(")", "").strip()
        return date

    def generate_type(self):
        type = self.film[1]
        return type.strip().lower()