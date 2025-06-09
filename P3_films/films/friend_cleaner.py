from .data import friends
from .friend import Friend


class FriendCleaner:
    def __init__(self):
        self.friends = friends

    @staticmethod
    def clean(data, library):
        name = data[0]
        if len(data) > 1:
            film_name = data[1]
            film = library.get_by_name(film_name)
        else :
            film = None
        return Friend(name, film)

    def list_from_data(self, library):
        result = []
        for data in self.friends:
            friend = self.clean(data, library)
            result.append(friend)
        return result