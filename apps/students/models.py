from django.db import models

# Create your models here.
class Student(models.Model):
    class Meta:
        db_table = 'Students'

    Name = models.CharField('Name',max_length= 50, db_index= True, blank=False, null = False)
    Email = models.EmailField('Email', blank=False, null=False, db_index= True)
    Grade = models.IntegerField('Grade', blank=False, null=False,)
    created_on = models.DateTimeField('CreatedOn', blank=False,auto_now_add=True)

    def __str__(self):
        return self.Name