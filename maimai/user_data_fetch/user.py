import json
import os


class User:
    def __init__(self, friend_code):
        self.friend_code = friend_code
        if os.path.exists(f'..\\..\\user\\{self.friend_code}.json'):
            self.icon_url = ''
            self.name = ''
            self.rating = 0
            self.title = ''
            self.song_score = ''
        else:
            print('a')

    def __load_user_file(self):
        with open(f'..\\..\\user\\{self.friend_code}.json') as f:
            data = json.load(f)
            self.icon_url = data['icon_url']
            self.name = data['name']
            self.rating = data['rating']
            self.title = data['title']

    def __load_song_score(self):
        pass


User('123')
