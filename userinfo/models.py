from django.db import models




class Savedata(models.Model):
    username = models.CharField(max_length=50)
    password = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.title


class Hotel(models.Model):
	name = models.CharField(max_length=50)
	hotel_Main_Img = models.ImageField(upload_to='images/')


TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

 
