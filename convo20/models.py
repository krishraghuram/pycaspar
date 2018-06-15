from django.db import models

# Create your models here.

class Student(models.Model):
	rollno = models.IntegerField(unique=True)
	name = models.CharField(max_length=100)
	programme = models.CharField(max_length=50)
	branch = models.CharField(max_length=50)

	class Meta:
		verbose_name="Student"
		verbose_name_plural="Students"

	def pretty_name(self):
		if self.name=="" or self.name is None:
			return self.rollno
		else: 
			return self.name
	pretty_name.short_description = "Name"