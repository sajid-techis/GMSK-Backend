from django.db import models
from apps.students.models import Student

# Create your models here.
class Subjects(models.Model):
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        db_table = 'subject'
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100, blank = False, null = False)
    marks_out_of = models.IntegerField(default=100, blank = True, null = True)
    marks_scored = models.IntegerField(blank=True, null = True)
    created_at = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    def __str__(self):
        return self.subject_name