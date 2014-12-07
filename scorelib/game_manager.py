import json

import db_manager
from utils import *

def match_expansion(flag, exp_id):
	return flag & 1<<exp_id

def get_games(game_id):
	return sorted(db_manager.get_games(game_id), key=lambda g:g.expansion_id)