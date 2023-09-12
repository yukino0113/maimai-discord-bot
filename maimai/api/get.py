"""
tables = IntlSheets, SheetExtras, SheetInternalLevels, SheetVersions, Sheets

IntlSheets= songId, type, difficulty
SheetExtras = songId, type, difficulty,
              noteCount.tap, noteCount.hold, noteCount.slide, noteCount.touch, noteCount.break, noteCount.total,
              noteDesigner
SheetInternalLevels = songId, type, difficulty, internalLevel
SheetVersions = songId, type, version
Sheets = songId, type, difficulty, level
SongExtra = songId, bpm, releaseDate
Songs = songId, category, title, artist, imageName, imageUrl, version, releaseDate, isNew, isLocked
"""
import sqlite3

sql_connection = sqlite3.connect(r"..\..\fetch_songs\data\maimai\db.sqlite3")
sql_connection.row_factory = lambda cursor, row: row[0]
cur = sql_connection.cursor()


def get_version_song_list(version: str) -> list:
    return cur.execute(f"SELECT songId FROM Songs WHERE version = '{version}'").fetchall()


def get_song_level(song_id: str, difficulty: str) -> float:
    if level := cur.execute(f"SELECT internalLevel FROM SheetInternalLevels "
                            f"WHERE songId='{song_id}' AND difficulty='{difficulty}'").fetchone():
        return level
    if level := cur.execute(f"SELECT level FROM Sheets "
                            f"WHERE songId='{song_id}' AND difficulty='{difficulty}'").fetchone():
        if '+' in level:
            return float(level[:-1] + '.7')
        else:
            return level
    return -1


sql_connection.close()