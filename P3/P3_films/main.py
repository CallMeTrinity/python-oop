"""Point d'entrée."""

# l'utilisation de pprint permet de mieux afficher les conteneurs.
from pprint import pprint
from films.library import Library
from films.friend_cleaner import FriendCleaner

def main():
    """Code client."""
    library = Library()

    films = library.films
    friends = FriendCleaner().list_from_data(library)

    print("Tous mes films:")
    pprint(films)
    print()
    print("Tous mes amis:")
    pprint(friends)
    print()

    library.sort_by_type()
    print("Mes films triés par type:")
    pprint(films)
    print()

    film = library.get_random_film()
    print(f"Film récupéré au hasard: {film}")
    print()

    films_lent = library.get_films_lent()
    print("J'ai prêté ces films:")
    pprint(films_lent)
    print()

    for film in films_lent:
        print(f"Le film '{film}' est chez", film.location)


if __name__ == "__main__":
    main()
