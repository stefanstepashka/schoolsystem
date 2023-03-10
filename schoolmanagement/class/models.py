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
    grade = models.FloatField()
    note = models.TextField(default=True, null=True)

class Exam(models.Model):
    name = models.CharField(max_length=120)
    format = models.CharField(max_length=20, choices=[("online", "Online"), ("in-person", "In-Person")], null=True)
    date = models.DateField()
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True,  default=1)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,  default=1 )
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, default=1, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, default=1)
    date_time = models.DateTimeField(null=True)

