from models import *

@model_get_optional_result
def get_player(pid):
	return Player.objects.filter(id=pid)

def get_games(gid):
	return Expansion.objects.filter(id=gid)

@model_get_optional_result
def get_match(mid):
	return Match.objects.filter(id=mid)

def get_match_by_game(gid):
	return Match.objects.filter(game_id=gid)

def get_match_by_player(pid):
	return Match.objects.filter(player_id=pid)

def get_scores_by_match(match_id):
	return Score.objects.filter(match_id=match_id)