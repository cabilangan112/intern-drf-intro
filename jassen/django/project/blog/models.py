from django.db import models

# Create your models here.\
class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    release_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    picture = models.ImageField(upload_to = 'static/media')
    date_modified = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

class Website(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=250)
    owner = models.CharField(max_length=200)
    logo =  models.ImageField(upload_to = 'static/media')
    date_modified = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)

class Breed(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    is_official = models.BooleanField(default=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)