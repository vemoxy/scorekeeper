import json

from constant import *
import db_manager
import game_manager
import player_manager
import score_manager
from utils import *

def get_match(match_id):
	match = db_manager.get_match(match_id)
	scores = score_manager.get_scores_by_match(match_id)
	games = game_manager.get_games(match.game_id)

	subscores_info = []
	roles_info = []
	bgcolor = DEFAULT_GAME_BG_COLOR

	for game in games:
		if game_manager.match_expansion(match.expansion_flag, game.expansion_id):
			game_extra = get_extra(game)
			subscores_info = union(subscores_info, game_extra[GameExtra.SUBSCORES])
			roles_info = union(roles_info, game_extra[GameExtra.ROLES].keys())
			bgcolor = game_extra.get('bgcolor', DEFAULT_GAME_BG_COLOR)

	player_scores = []
	for score in scores:
		player_score = {
			'player_id': score.player_id,
			'player_name': player_manager.get_player_name(score.player_id),
			'score': score.score,
		}
		score_extra = get_extra(score)
		subscores = score_extra[GameExtra.SUBSCORES]
		if subscores:
			player_score[GameExtra.SUBSCORES] = subscores
		roles = score_extra[GameExtra.ROLES]
		if roles:
			player_score[GameExtra.ROLES] = roles
		player_scores.append(player_score)
	return {
		'game_name': game.name,
		'description': match.description,
		'game_design': {'banner': game.banner, 'bgcolor': bgcolor},
		'scores': player_scores,
		'subscores_info': subscores_info,
		'roles_info': roles_info,
	}