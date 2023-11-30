from django.db import models

# Create your models here.

class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=100)
    u_age = models.IntegerField()
    u_gender = models.CharField(max_length=10)

    class Meta:
        db_table = "User"

