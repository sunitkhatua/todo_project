from django.db import models
from django.contrib.auth.models import User
class Todo(models.Model):
    status_choices = [
    ('Open','Open'),
    ('Working','Working'),
    ('Done','Done'),
    ('Overdue','Overdue'),
    ]
    Time=models.TimeField(auto_now = True)
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    Date = models.DateField(auto_now=False, auto_now_add=False)
    Tag = models.CharField(max_length=100,blank=True)
    Status = models.CharField(max_length=20 , choices=status_choices,default='OPEN')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
