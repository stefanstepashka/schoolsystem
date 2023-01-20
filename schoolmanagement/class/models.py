from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=120)
    student_id = models.CharField(max_length=20, default=None, null=True)
    teachers = models.ManyToManyField('Teacher', through='Enrollment')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=120)
    employee_id = models.CharField(max_length=20, default=None, null=True)
    students = models.ManyToManyField(Student, through='Enrollment')

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=120)
    students = models.ManyToManyField(Student, through='Enrollment')
    teacher = models.ManyToManyField(Teacher, through='Enrollment')

    def __str__(self):
        return self.name

class Schedule(models.Model):
    day = models.IntegerField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.day + ' ' + str(self.start_time)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("student", "class_name"), ("teacher", "class_name"))


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.FloatField(max_digits=3, decimal_places=2)
    text = models.TextField()
