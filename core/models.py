from django.db import models

# Create your models here.

class Tasks(models.Model):
        inprogress="IN"
        completed="CO"
        notassigned="NA"
        CHOICES = {
        inprogress:"inprogress",
        completed :"completed",
        notassigned :"notassigned",       
        } 

        title=models.CharField(max_length=20)
        description=models.CharField(max_length=32)
        deadline=models.DateTimeField()
        priority=models.IntegerField()
        status=models.CharField(max_length=2,choices=CHOICES,default=notassigned)
        
        
        location=models.CharField(max_length=20)
