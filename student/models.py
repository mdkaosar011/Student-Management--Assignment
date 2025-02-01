from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Student_Info(models.Model):
    courses =(
        ('Python', 'Python'),
        ("Django",'Django'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
        ('ML', 'Machine Learning'),
        ('DS', 'Data Science'),
        )
    
    sID = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=75, null= False)
    email = models.EmailField(null= True)
    phone_number = PhoneNumberField(region="BD")
    course = models.CharField(max_length=50, choices= courses)


    def __str__(self):
        return  f"{self.sID} - {self.name}"
    

class CourseInfo(models.Model):
    course_name = models.CharField(max_length=50)
