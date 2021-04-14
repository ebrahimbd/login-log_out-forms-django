from django.db import models




class Savedata(models.Model):
    username = models.CharField(max_length=50)
    password = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.title