from django.db import models

# Create your models here.

class Batches(models.Model):
    batch_year = models.IntegerField()
    def __str__(self):
        return str(self.batch_year) #if we won't do this then the name of the field will appear as tasklist object. 

