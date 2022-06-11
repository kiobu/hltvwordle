from pathlib import Path
from fetcher import HLTVFetch, LiquipediaFetch
import random
import datetime


class PlayerOfTheDay:
    @staticmethod
    def choose_player():
        d = HLTVFetch.teams
        team = list(d.keys())[random.randint(0, len(d))]
        player = d[team][random.randint(0, 4)]

        return player

    @staticmethod
    def choose_player_and_save():
        return PlayerOfTheDay.player_data(PlayerOfTheDay.choose_player())

    @staticmethod
    def player_data(player):
        fp = Path(f'player_{datetime.date.today()}.txt')
        fp.touch(exist_ok=True)
        with open(fp, 'w') as f:
            f.write(str(player))

