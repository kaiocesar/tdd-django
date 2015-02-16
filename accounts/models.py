from __future__ import absolute_import
from django.db import models


class Accounts(models.Model):
	id = models.IntegerField(primary_key=True)
	agencia = models.IntegerField()
	num_conta = models.IntegerField()
	tipo_conta = models.CharField(max_length=3)
	status = models.CharField(max_length=1)
	created_at = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'accounts'
		verbose_name = 'Account'
		verbose_name_plural = 'Accounts'


	def CheckAccount(self, number=None):
		if (not number):
			return False

		if (numer == '123'):
			return True

		return False
