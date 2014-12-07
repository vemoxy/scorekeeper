from django.db import models, connections
from django.db.models.fields import BigIntegerField

class PositiveBigIntegerField(BigIntegerField):
	empty_strings_allowed = False
	def db_type(self, connection):
		return "bigint UNSIGNED"
	def formfield(self, **kwargs):
		defaults = {'min_value': 0, 'max_value': BigIntegerField.MAX_BIGINT * 2 - 1}
		defaults.update(kwargs)
		return super(PositiveBigIntegerField, self).formfield(**defaults)

class PositiveTinyIntegerField(models.PositiveSmallIntegerField):
	def db_type(self, connection):
		return "tinyint unsigned"
	def formfield(self, **kwargs):
		defaults = {'min_value': 0, 'max_value': 255}
		defaults.update(kwargs)
		return super(PositiveTinyIntegerField, self).formfield(**defaults)

def model_get_optional_result(func):
	def _func(*args, **kwargs):
		results = func(*args, **kwargs)
		if not results:
			return None
		return results[0]
	return _func