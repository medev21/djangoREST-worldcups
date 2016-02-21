from django.db import models

# Create your models here.

class Worldcup(models.Model):
    created = models.DateTimeField(auto_now_add = True) #created date time
    title = models.CharField(max_length = 100, blank = True, default = '')
    description = models.TextField()
    year = models.IntegerField(default = 2016)
    winner = models.CharField(max_length =100, blank = True, default = '')
    runner_up = models.CharField(max_length = 100, blank = True, default = '')
    owner = models.ForeignKey('auth.User', related_name = 'worldcups')

    class Meta:
        ordering = ('created',)
