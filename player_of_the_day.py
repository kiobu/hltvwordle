from fetcher import HLTVFetch
import random


class PlayerOfTheDay:
    @staticmethod
    def choose_player():
        d = HLTVFetch.teams
        team = list(d.keys())[random.randint(0, len(d))]
        player = d[team][random.randint(0, 4)]

        return player

    @staticmethod
    def choose_player_and_save():
        player = PlayerOfTheDay.choose_player()
        PlayerOfTheDay.player = player
