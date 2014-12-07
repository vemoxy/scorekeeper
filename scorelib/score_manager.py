import json

import db_manager

def get_scores_by_match(match_id):
	return sorted(db_manager.get_scores_by_match(match_id), key=lambda s:s.score, reverse=True)