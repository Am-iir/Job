from django.db import models

# Create your models here.

class SignUp(models.Model):
    full_name=models.CharField(max_length=100) #max length is required field
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True , auto_now=False) #means when the field is created the time stamp is added

    def __str__(self): #unicode
        return self.email

class Job(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False )

    def __str__(self): #unicode
        return self.title

    class Meta:
        ordering = ["-timestamp"]


    


