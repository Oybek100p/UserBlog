from django.db import models


Countries = [
    ('Germany','Germany'),
    ('France','France'),
    ('United States Of Amerika','United States Of Amerika'),
    ('Uzbekistan','Uzbekistan'),
    ('Egypt','Egypt'),
]

class Creator(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='image/')
    bio = models.TextField()
    country = models.CharField(choices = Countries)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Creator, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='image/')
    hashtags = models.TextField()
    video = models.URLField(blank=True, null=True)
    country = models.CharField(choices = Countries)
    add_date = models.DateTimeField(auto_now_add=True)



# Create your models here.
