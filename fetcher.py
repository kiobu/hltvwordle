import requests
from collections import OrderedDict
from requests import Response
from bs4 import BeautifulSoup
from pathlib import Path


class ResponseParser:
    def __init__(self, response: Response):
        self.parsed: BeautifulSoup = BeautifulSoup(response.content, 'html.parser')

    def __call__(self):
        return self.parsed


class HLTVFetch:
    baseUrl = 'https://www.hltv.org/ranking/teams'
    teams = OrderedDict()

    @staticmethod
    def update():
        parser = ResponseParser(requests.get(HLTVFetch.baseUrl, headers={'User-Agent': 'csgo-wordle'}))
        HLTVFetch.parse_body(parser())

    @staticmethod
    def parse_body(soup: BeautifulSoup):
        for div in soup.find_all('div', ['ranked-team', 'standard-box']):
            team = div.find('span', 'name')

            if not team:
                continue

            team = team.text

            HLTVFetch.teams[team] = []

            for player_line in div.find_all('div', 'rankingNicknames'):
                player = player_line.find('span').text

                HLTVFetch.teams[team].append(player)

    # Write mock data once, so we're not scraping HLTV every time we are debugging.
    @staticmethod
    def write_mock_data():
        HLTVFetch.update()
        fp = Path('mock_data.txt')
        fp.touch(exist_ok=True)
        with open(fp, 'w') as f:
            f.write(str(HLTVFetch.teams))

class LiquipediaFetch:
    baseUrl = 'https://liquipedia.net/counterstrike'
