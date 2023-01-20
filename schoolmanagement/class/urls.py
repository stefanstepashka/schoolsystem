from django.contrib import admin
from django.urls import path
from .views import ClassListView, \
    ClassCreateView, ClassUpdateView, ClassDetailView, \
    TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDetailView, EnrollmentCreateView, \
    StudentListView, StudentCreateView, StudentUpdateView, StudentDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classes/', ClassListView.as_view(), name='class_list'),
    path('classes/create/', ClassCreateView.as_view(), name='class_create'),
    path('classes/<int:pk>/edit/', ClassUpdateView.as_view(), name='class_edit'),
    path('classes/<int:pk>/', ClassDetailView.as_view(), name='class_detail'),

    #Teachers
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),

    #Students

    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('enroll/', EnrollmentCreateView.as_view(), name='enroll'),

]
