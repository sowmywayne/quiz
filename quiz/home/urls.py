from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_quiz', views.create_quiz, name='create_quiz'),
    path('store_question', views.store_question, name='store_question'),
    path('submition', views.submition, name='submition'),
]