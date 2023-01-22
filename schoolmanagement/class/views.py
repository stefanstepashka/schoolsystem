
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from .models import Class, Student, Teacher, Enrollment, Grade, Exam, Schedule
from django.urls import reverse_lazy

# Create your views here.
from django.db.models import Q

class ClassDetailView(DetailView):
    model = Class
    template_name = 'class/class_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enrollments'] = Enrollment.objects.filter(class_name=self.object)
        context['students'] = Student.objects.filter(enrollment__in=context['enrollments'])
        context['teachers'] = Teacher.objects.filter(enrollment__in=context['enrollments'])
        return context


class ClassListView(ListView):
    model = Class
    template_name = 'class/class_list.html'
    context_object_name = 'classes'


class ClassCreateView(CreateView):
    model = Class
    fields = ['name']
    template_name = 'class/class_form.html'
    success_url = reverse_lazy('class_list')


class ClassUpdateView(UpdateView):
    model = Class
    fields = ['name']
    template_name = 'class/class_form.html'
    success_url = reverse_lazy('class_list')


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher/teacher_list.html'
    context_object_name = 'teachers'


class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['name', 'employee_id']
    template_name = 'teacher/teacher_form.html'
    success_url = reverse_lazy('teacher_list')


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['name', 'employee_id']
    template_name = 'teacher/teacher_form.html'
    success_url = reverse_lazy('teacher_list')


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher/teacher_list.html'


class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(
                Q(name__icontains=query)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'student_id']
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'student_id']
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('student_list')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.filter(enrollment__student=self.object)
        context['enrollments'] = Enrollment.objects.filter(student=self.object)
        context['exams'] = Exam.objects.filter(class_name__enrollment__student=self.object)
        context['schedule'] = Schedule.objects.filter(student=self.object)
        return context


class EnrollmentCreateView(CreateView):
    model = Enrollment
    fields = ['student', 'teacher', 'class_name']
    template_name = 'enrollment_form.html'
    success_url = reverse_lazy('class_list')


class ExamListView(ListView):
    model = Exam
    template_name = 'exam/exam_list.html'
    context_object_name = 'exams'


class ExamCreateView(CreateView):
    model = Exam
    fields = ['name', 'date', 'class_name', 'format']
    template_name = 'exam/exam_form.html'
    success_url = reverse_lazy('exam_list')


class ExamUpdateView(UpdateView):
    model = Exam
    fields = ['name', 'date', 'class_name']
    template_name = 'exam/exam_form.html'
    success_url = reverse_lazy('exam_list')


class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'exam/exam_confirm_delete.html'
    success_url = reverse_lazy('exam_list')


class ScheduleListView(ListView):
    model = Schedule
    template_name = 'schedule/schedule_list.html'
    context_object_name = 'schedules'


class ScheduleCreateView(CreateView):
    model = Schedule
    fields = ['student', 'class_name', 'exam', 'date_time']
    template_name = 'schedule/schedule_form.html'
    success_url = reverse_lazy('schedule_list')



class ScheduleUpdateView(UpdateView):
    model = Schedule
    fields = ['student', 'class_name', 'exam', 'date_time']
    template_name = 'schedule/schedule_form.html'
    success_url = reverse_lazy('schedule_list')


class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'schedule/schedule_confirm_delete.html'
    success_url = reverse_lazy('schedule_list')


class Home(TemplateView):
    template_name = 'base.html'