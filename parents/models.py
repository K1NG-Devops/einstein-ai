from django.db import models
from students.models import Student
from django.urls import reverse

class Parent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True) # unique=True to make sure that the email is unique
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    child = models.ForeignKey(Student, on_delete=models.CASCADE) # create a many-to-one relationship with the Student model

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('parents:parent_detail', args=(str(self.id)))
