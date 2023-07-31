from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    class Meta:
        managed = False
        db_table = "Place"