from . views import *
from django.urls import path

urlpatterns = [
    path('student',get_student,name='student'),
    path('student/<int:id>',get_student,name='student')

]
