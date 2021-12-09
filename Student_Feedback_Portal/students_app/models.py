from django.db import models

# Create your models here.

class Feedback(models.Model):
    professor = models.TextField()
    batch = models.TextField()
    response1 = models.IntegerField()
    response2 = models.IntegerField()
    response3 = models.IntegerField()
    response4 = models.IntegerField()
    response5 = models.IntegerField()
    def __str__(self):
        return self.professor + "'s Feedback" #if we won't do this then the name of the field will appear as tasklist object. 


class Questions(models.Model):
    question = models.TextField()

    def __str__(self):
        return self.question