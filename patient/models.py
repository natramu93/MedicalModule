from django.db import models
from django.urls import reverse
# Create your models here.
class Patient(models.Model):
    fname = models.CharField(max_length=246)
    mname = models.CharField(max_length=246,blank=True)
    lname = models.CharField(max_length=246)
    gender = models.CharField(max_length=6, choices=(('Male','Male'),('Female','Female')), default='Male')
    dob = models.DateField()

    def get_absolute_url(self):
        return reverse("patient:detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.fname

