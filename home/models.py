from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class User(models.Model):
	user 		= models.OneToOneField(User, on_delete=models.CASCADE)
	name		= models.CharField(max_length = 20)
	age			= models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(2)])

