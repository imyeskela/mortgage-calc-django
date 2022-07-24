from django.db import models


class Mortgage(models.Model):
    bank_name = models.CharField('Name of the Bank', max_length=100)
    rate = models.FloatField('Mortgage Rate')
    payment = models.PositiveIntegerField('Payment')
    price = models.PositiveIntegerField('Price')

    def __str__(self):
        return f'{self.bank_name}; Mortgage Rate: {self.rate}; Price: {self.price}'
    