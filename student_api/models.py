from django.db import models

# Create your models here.
class Path(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"
    
    #to get all students for related path student_set or with
    
    #related name students
    
class Student(models.Model):
    path = models.ForeignKey(Path,on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    number = models.IntegerField(blank=True, null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return f'{self.first_name} - {self.last_name}'
        