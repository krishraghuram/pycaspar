from django.db import models

# Create your models here.

class Student(models.Model):
	orderno   = models.IntegerField(unique=True)
	rollno    = models.IntegerField(unique=True)
	name      = models.CharField(max_length=100)
	programme = models.CharField(max_length=50)
	branch    = models.CharField(max_length=50)

	class Meta:
		verbose_name        = "Student"
		verbose_name_plural = "Students"

	def pretty_name(self):
		if self.name=="" or self.name is None:
			return self.rollno
		else: 
			return self.name
	pretty_name.short_description = "Name"


class VIP(models.Model):
	orderno     = models.IntegerField(unique=True)
	name        = models.CharField(max_length=100)
	designation = models.CharField(max_length=100)
	
	class Meta:
		verbose_name="VIP"
		verbose_name_plural="VIPs"

	def pretty_name(self):
		if self.name=="" or self.name is None:
			return self.designation
		else: 
			return self.name
	pretty_name.short_description = "Name"


class Medal(models.Model):
	orderno   = models.IntegerField(unique=True)
	rollno    = models.IntegerField(unique=True)
	medal     = models.CharField(max_length=100)
	name      = models.CharField(max_length=100)
	programme = models.CharField(max_length=50)
	branch    = models.CharField(max_length=50)

	class Meta:
		verbose_name="Medal Winner"
		verbose_name_plural="Medal Winners"

	def pretty_name(self):
		if self.name=="" or self.name is None:
			return self.medal
		else: 
			return self.name
	pretty_name.short_description = "Name"