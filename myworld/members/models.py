from django.db import models

class Members(models.Model):
    firstname = models.CharField(max_length=255) # will contain the first name of the members.
    lastname = models.CharField(max_length=255)  # the members' last name

