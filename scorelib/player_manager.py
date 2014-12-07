import db_manager

def get_player_name(player_id):
	return db_manager.get_player(player_id).name