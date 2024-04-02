from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Post(models.Model):
    imageURL=models.ImageField(upload_to='evlonPosts/')
    caption=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    Time=models.CharField(max_length=100)
    timeRemaining=models.IntegerField()
    Attendance=models.IntegerField()
    likesCount=models.IntegerField()
    commentsCount=models.IntegerField()
    smallProfile=models.ImageField(upload_to='evlonPosts/')
    name=models.CharField(max_length=50)
    counter=models.IntegerField()
    
    class Meta:
        db_table="EvlonPosts"
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments")
    description=models.TextField()
    likesCount=models.IntegerField()
    
    class Meta:
        db_table="EvlonComments"
    
    def __str__(self):
        return f"{self.user.username}'s comment"
    
    
