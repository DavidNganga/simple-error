from django.db import models

# Create your models here.
class Error(models.Model):
    language = models.CharField(max_length = 25,null = True)
    error = models.CharField(max_length=250,null=True)
    explanation = models.TextField(max_length=200,null=True)

class Comment(models.Model):
    error = models.ForeignKey(Error, on_delete=models.CASCADE,null=True)
    post = models.TextField(max_length=200,null=True)
