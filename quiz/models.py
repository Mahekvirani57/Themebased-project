from django.db import models
from edustage.models import Destination

# Create your models here.


class Quiz(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    correct = models.IntegerField()

    def __str__(self):
        return self.question

