from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Candidate(models.Model):
	name = models.CharField(max_length=50)
	location_city=models.CharField(max_length=50)
	location_country=models.CharField(max_length=50)

class Experience(models.Model):
	candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
	company_name = models.CharField(max_length=100)
	job_role = models.CharField(max_length=100)
	company_location=models.CharField(max_length=100)
	Years_worked=models.IntegerField(default=0)

class Education(models.Model):
	candidate_id=models.ForeignKey(Candidate, on_delete=models.CASCADE)
	institute_name = models.CharField(max_length=200)
	institute_location = models.CharField(max_length=200)
	start_year=models.IntegerField(default=0)
	end_year=models.IntegerField(default=0)
