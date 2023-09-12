from maimai.api.get import get_version_song_list


def get_nameplate_result(version: str, ) -> None:
    song_list = get_version_song_list(version)
    pass

print(get_nameplate_result('GreeN'))