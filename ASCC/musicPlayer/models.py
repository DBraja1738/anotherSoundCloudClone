from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    listen_count=models.PositiveIntegerField(default=0)



class Playlist(models.Model):
    name=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    songs=models.ManyToManyField("Song")