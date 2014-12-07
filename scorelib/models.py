from common.model_utils import *

class Player(models.Model):
	name = models.CharField(max_length=50)
	class Meta:
		db_table = u'player_tab'

class Expansion(models.Model):
	game_id = PositiveBigIntegerField()
	expansion_id = PositiveTinyIntegerField()
	base_set = models.BooleanField()
	name = models.CharField(max_length=100)
	icon = models.CharField(max_length=1024)
	banner = models.CharField(max_length=1024)
	extra_data = models.TextField()
	class Meta:
		db_table = u'expansion_tab'

class Match(models.Model):
	game_id = PositiveBigIntegerField()
	expansion_flag = PositiveBigIntegerField()
	player_id = PositiveBigIntegerField()
	description = models.CharField(max_length=1024)
	class Meta:
		db_table = u'match_tab'

class Score(models.Model):
	match_id = PositiveBigIntegerField()
	player_id = PositiveBigIntegerField()
	score = models.PositiveIntegerField()
	extra_data = models.TextField()
	class Meta:
		db_table = u'score_tab'