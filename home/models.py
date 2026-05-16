from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class View(models.Model):
    vid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Member(models.Model):
    mid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Pyment(models.Model):
    mpid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    cardno=models.CharField(max_length=255)
    carddate=models.CharField(max_length=255)
    secucode=models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Profile(models.Model):
    uid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uimages/',null=True)
    email = models.CharField(max_length=255)
    profilbio = models.TextField()
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    

    def __str__(self):
        return self.username
    
class Blogwrite(models.Model):
    bwid= models.BigAutoField(primary_key=True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="posts", null=True, blank=True)
    cimage=models.ImageField(upload_to='bimages/',null=True)
    title= models.CharField(max_length=255)
    subtitle= models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author.username) if self.author else "Unknown Author"
    
class Comment(models.Model):
    cid=models.BigAutoField(primary_key=True)
    cusername = models.CharField(max_length=255)
    comment= models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)
    bwid = models.ForeignKey(Blogwrite, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.cusername
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogwrite, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    ldate = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'blog', 'comment')
    
    def __str__(self):
        return self.user.username
    
class Save(models.Model):
    sid=models.BigAutoField(primary_key=True)
    susername=models.ForeignKey(Profile, on_delete=models.CASCADE)
    bwid = models.ForeignKey(Blogwrite, on_delete=models.CASCADE, null=True, blank=True)

class Follow(models.Model):
    fid=models.BigAutoField(primary_key=True)
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='following_set')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='followers_set')
    fdate = models.DateTimeField(auto_now_add=True)

class Contect(models.Model):
    cid = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    

    def __str__(self):
        return str(self.user.username)
