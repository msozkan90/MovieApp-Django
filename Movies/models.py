from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, TextField,DateTimeField
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.name
class Actor(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    films=models.CharField(blank=True,max_length=40)
    biography=models.TextField(max_length=400)
    genders = (
        ('M','Male'),
        ('F','Female'),  
    )
    gender=models.CharField(max_length=1, choices=genders)
    photos=models.ImageField()
    profile_photos=models.ImageField()
    slug = models.SlugField(default="", blank=True, null=False, db_index=True, unique=True)
    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url=self.photos.url
        except:
            url=''
        return url


class Film(models.Model):
    title=models.CharField(max_length=40)
    Cast=models.ManyToManyField(Actor)
    date_added = models.DateTimeField(auto_now_add=False)
    summary=models.TextField(max_length=400)
    category=models.ManyToManyField(Category)
    photos=models.ImageField()
    fragman=models.FileField(blank="True")
    slug = models.SlugField(default="", blank=True, null=False, db_index=True, unique=True)
    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url=self.photos.url
        except:
            url=''
        return url



class Film_rate(models.Model):
    title=models.ForeignKey(Film,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    rate=models.IntegerField(        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)],default=0)
    avg_rate=models.DecimalField(max_digits=5, decimal_places=2,default=0)

