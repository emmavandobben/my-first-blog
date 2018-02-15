# Create your models here. (objecten)

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(
        max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True,
        null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Label(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    label = models.CharField(
        max_length=200)

'''
Class            definieer je een class
Post             naam van je oject (model)
models.Model     betekend dat Post een django model is. 
                 Django weet nu dat het in de db moet.

author, title    dit zijn properties
.ForeignKey      dit geeft het type aan; relatie tot ander model(object), hier User.
.CharField       type text met gelimiteerd aantal characters
.TextField       text zonder limiet
DateTimeField    datum en tijd

def              dit is een methode (lowercase & underscores worden gebruikt)

'''