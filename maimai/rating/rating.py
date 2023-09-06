def get_song_rating(song_name: str, difficulty: str, achievement_rate: float) -> float:
    if achievement_rate >= 100.5:
        return get_song_level(song_name, difficulty) * 100.5 * get_coefficient(achievement_rate)
    else:
        return get_song_level(song_name, difficulty) * achievement_rate * get_coefficient(achievement_rate)


def get_coefficient(achievement_rate: float) -> float:
    if achievement_rate >= 100.5:
        return 22.4
    elif achievement_rate >= 100:
        return 21.6
    elif achievement_rate >= 99.5:
        return 21.1
    elif achievement_rate >= 99:
        return 20.8
    elif achievement_rate >= 98:
        return 20.3
    elif achievement_rate >= 97:
        return 20
    elif achievement_rate >= 94:
        return 16.8
    elif achievement_rate >= 90:
        return 15.2
    else:
        return 13.6


def get_song_level(song_name: str, difficulty: str) -> float:
    pass


class Rating:
    def __init__(self):
        self.recent_best = self.__get_recent_best_dict()
        self.history_best = self.__get_history_best_dict()

    @staticmethod
    def __get_recent_best_dict() -> dict:
        pass

    @staticmethod
    def __get_history_best_dict() -> dict:
        pass


