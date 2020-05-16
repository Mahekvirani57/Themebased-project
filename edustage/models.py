from django.db import models

# Create your models here.
class Destination(models.Model):
	
	name = models.CharField(max_length=200)
	img = models.ImageField(upload_to='pics')
	price = models.IntegerField()
	author = models.CharField(max_length=200)
	ref = models.CharField(max_length=100, default="tutorial")
	

	def __str__(self):
		return self.name
			
class sample(models.Model):
	name = models.CharField(max_length=200)
	field_name = models.URLField(max_length=200)
	