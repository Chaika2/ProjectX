from django.db import models

class Taksk(models.Model):
    title = models.CharField('Куку', max_length=50)
    task = models.TextField('Описаниее')

def __str__(self):
    return self.title