from django.db import models


class Mortgage(models.Model):
    bank_name = models.CharField('Name of the Bank', max_length=100)
    rate = models.FloatField('Mortgage Rate')
    payment = models.IntegerField('Payment')

    def __str__(self):
        return f'Name - {self.bank_name}; Mortgage Rate: {self.rate}'
    