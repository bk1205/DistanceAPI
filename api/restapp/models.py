from django.db import models

'''
    This is Distance model, a blueprint of table which will be created in database to store queries <city1, 
    city2> to get travel distance, so that next time when same query can be resolved by just database lookup.
'''


class Distance(models.Model):
    id = models.AutoField(primary_key=True)
    city1 = models.CharField(max_length=100)
    city2 = models.CharField(max_length=100)
    distance = models.CharField(max_length=100)
    class Meta:
        unique_together = ('city1', 'city2')
