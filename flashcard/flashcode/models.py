from django.db import models

# Create your models here.

class Flashcard(models. Model):
    title = models.CharField(max_length=200)
    defination = models.CharField(max_length=200  , null=True)    
    description = models.CharField(max_length=200 , null=True)
    remembred = models.BooleanField(default= False)
    date_created = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.title