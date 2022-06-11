from fastapi import FastAPI
import schedule
from fetcher import HLTVFetch
from player_of_the_day import PlayerOfTheDay
from collections import OrderedDict

DEBUG = True

# Should always be true at startup.
# if not HLTVFetch.teams:
    # HLTVFetch.update()

if DEBUG:
    with open('mock_data.txt') as f:
        HLTVFetch.teams = OrderedDict(eval(f.readline()))

app = FastAPI()


@app.get("/")
async def root():
    return "csgo wordle"


@app.get("/write-mock-data")
async def write_mock_data():
    HLTVFetch.write_mock_data()


@app.get("/debug")
async def debug():
    print(PlayerOfTheDay.choose_player())

schedule.every().day.at("11:59").do(HLTVFetch.update)
schedule.every().day.at("12:00").do(PlayerOfTheDay.choose_player_and_save)
