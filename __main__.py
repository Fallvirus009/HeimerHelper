from helpers import get_static_player_data, get_match_history, get_static_live_data, getLivePlayerData

summoner = 'SUMM_NAME'

print(get_static_player_data(summoner))
print(get_static_player_data(summoner)['puuid'])
print(get_match_history(summoner, 5))
print(getMatchData(get_match_history(summoner, 5)[0]))
print(getLivePlayerData())
