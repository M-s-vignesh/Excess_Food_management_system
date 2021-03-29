from django.db import models

# Create your models here.
class food_database(models.Model):
	Enter_Location=models.CharField(max_length=100)
	Enter_The_Name_Of_Organization=models.CharField(max_length=1000)
	Enter_Address=models.CharField(max_length=1000)
	Enter_Food_Menu=models.CharField(max_length=1000)
	Enter_Quantity_Per_Person=models.CharField(max_length=1000)
	Time_To_Pickup_Range_With_Date=models.CharField(max_length=1000)