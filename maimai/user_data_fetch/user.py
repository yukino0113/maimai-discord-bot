import pandas as pd
import json
import os


class User:
    def __init__(self, discord_id, friend_id):
        self.discord_id = discord_id
        self.friend_id = friend_id
        self.info_path = f'maimai/user/{self.discord_id}.json'
        self.song_path = f'maimai/user/{self.discord_id}.csv'

        if os.path.exists(self.info_path):
            self.__load_user_file()
            self.__load_song_score()
        else:
            with open(self.info_path):
                self.__save_user_data()
            with open(self.song_path, 'w'):
                pass

    def set_attribute(self, key, value):
        self.__dict__[key] = value
        self.__save_user_data()

    def __save_user_data(self):
        with open(self.info_path, 'w+') as j:
            json.dump(self.__dict__, j)

    def __save_song_score(self, score):
        # todo: save song score to csv
        pass

    def __load_user_file(self):
        with open(self.info_path, 'r') as j:
            d = json.load(j)
            # todo: load song score from csv
        print(d)

    def __load_song_score(self):
        self.song_score = pd.read_csv(self.song_path)
