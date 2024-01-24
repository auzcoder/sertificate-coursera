from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=200)
    choice_text = models.TextField()
    vote = models.IntegerField()

    def __str__(self):
        return self.question