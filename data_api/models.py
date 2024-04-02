from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator

# Create your models here.

class Department(models.Model):
    name = models.CharField(validators=[MinLengthValidator(2,'Department name must contain at least 2 characters')]) 
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(validators=[MinLengthValidator(2,'first name must contain at least 2 characters')]) 
    last_name = models.CharField(validators=[MinLengthValidator(2,'last name must contain at least 2 characters')]) 
    title = models.CharField(blank=True) # todo make optional
    email = models.EmailField(validators=[EmailValidator(message='Enter a valid email address')])
    image = models.ImageField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


