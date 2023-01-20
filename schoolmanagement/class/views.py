from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Class, Student, Teacher, Enrollment
from django.urls import reverse_lazy
# Create your views here.


class ClassDetailView(DetailView):
    model = Class
    template_name = 'class_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enrollments'] = Enrollment.objects.filter(class_name=self.object)
        context['students'] = Student.objects.filter(enrollment__in=context['enrollments'])
        context['teachers'] = Teacher.objects.filter(enrollment__in=context['enrollments'])
        return context


class ClassListView(ListView):
    model = Class
    template_name = 'class_list.html'
    context_object_name = 'classes'


class ClassCreateView(CreateView):
    model = Class
    fields = ['name']
    template_name = 'class_form.html'
    success_url = reverse_lazy('class_list')


class ClassUpdateView(UpdateView):
    model = Class
    fields = ['name']
    template_name = 'class_form.html'
    success_url = reverse_lazy('class_list')


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'
    context_object_name = 'teachers'


class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['name', 'employee_id']
    template_name = 'teacher_form.html'
    success_url = reverse_lazy('teacher_list')


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['name', 'employee_id']
    template_name = 'teacher_form.html'
    success_url = reverse_lazy('teacher_list')


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher_list.html'


class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'


class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'student_id']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'student_id']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'


class EnrollmentCreateView(CreateView):
    model = Enrollment
    fields = ['student', 'teacher', 'class_name']
    template_name = 'enrollment_form.html'
    success_url = reverse_lazy('class_list')

