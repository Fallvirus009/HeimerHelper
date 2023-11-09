import requests
import json
import time
import http

apiKey = 'RGAPI-7274e517-dc78-441c-874d-e5a55cbd7d9a'
accRegion = 'na1'
region = 'americas'

def get_static_player_data(name):
    url = f'https://{accRegion}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}'

    params = {
        'X-Riot-Token': apiKey
    }

    response = requests.get(url, headers = params)

    if response.status_code == 200:
        data = json.loads(response.text)
        return(data)
    else:
        return f"Error: {response.status_code}"

def get_match_history(name, count):
    puuid = get_static_player_data(name)['puuid']
    url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?&count={count}'

    params = {
        'X-Riot-Token': apiKey
    }

    response = requests.get(url, headers = params)

    if response.status_code == 200:
        data = json.loads(response.text)
        return(data)
    else:
        return f"Error: {response.status_code}"

def getMatchData(matchID):
    url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{matchID}'

    params = {
        'X-Riot-Token': apiKey
    }

    response = requests.get(url, headers = params)

    if response.status_code == 200:
        data = json.loads(response.text)
        return(data)
    else:
        return f"Error: {response.status_code}"

def get_static_live_data(summonerID):
    url = f'https://{accRegion}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summonerID}'
    
    params = {
        'X-Riot-Token': apiKey
    }

    response = requests.get(url, headers = params)

    if response.status_code == 200:
        data = json.loads(response.text)
        return(data)
    elif response.status_code == 404:
        return "Summoner is not in a game."
    else:
        return f"Error: {response.status_code}"

def getLivePlayerData():
    url = 'https://127.0.0.1:2999/liveclientdata/allgamedata'

    response = requests.get(url, verify='riotgames.pem')

    return response.text