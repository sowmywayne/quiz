from django.db import models
# Create your models here.

class Question(models.Model):
  rmdID = models.CharField(max_length=200)
  qnt = models.CharField(max_length=300)
  opt1 = models.CharField(max_length=100)
  opt2 = models.CharField(max_length=100)
  opt3 = models.CharField(max_length=100)
  answer = models.CharField(max_length=100)

  def __str__(self):
    return self.qnt

class Quiz(models.Model):
  rm = models.CharField(max_length=200)
  title = models.CharField(max_length=30)

  def __str__(self):
    return self.title    