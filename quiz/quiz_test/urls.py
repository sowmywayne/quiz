from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('quize_questions', views.quize_questions, name='quize_questions'),
  path('view_answer', views.view_answer, name='view_answer'),
]