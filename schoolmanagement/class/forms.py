from django import forms


from .models import Enrollment, Schedule, Student

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'teacher', 'class_name']


class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['student', 'class_name', 'exam', 'date_time']

    def __init__(self, class_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.filter(enrollment__class_id=class_id)