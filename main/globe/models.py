from django.db import models

# Create your models here.

class anime(models.Model):
    Anime = models.CharField(max_length=100)
    Animejap = models.CharField(primary_key=True ,max_length=100)
    Desciption = models.TextField()
    Ratings = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    class Meta:
        app_label = 'globe'
        db_table = 'anime'
