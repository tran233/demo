from django.db import models

# Create your models here.
class Like(models.Model):
    uid = models.IntegerField()
    wid = models.IntegerField()
