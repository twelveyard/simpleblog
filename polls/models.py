from django.db import models

# Create your models here.
from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name