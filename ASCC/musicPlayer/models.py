from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    
    duration=models.CharField(max_length=20)
    
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    listen_count=models.PositiveIntegerField(default=0)
    description=models.TextField(default="")

    likes=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    



class Playlist(models.Model):
    name=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    songs=models.ManyToManyField("Song")

    def __str__(self):
        return self.name

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    song=models.ForeignKey("Song",on_delete=models.CASCADE,related_name="comments")
    body=models.TextField()
    createdAt=models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
