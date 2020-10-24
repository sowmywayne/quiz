from django.shortcuts import render
from .models import Question
from .models import Quiz
import uuid

# Create your views here.
QUIZ_COUNT = 1
ID = 0
def index(request):
  return render(request, 'home.html', {'name': 'sowmy'})

def create_quiz(request):
  global ID
  ID = uuid.uuid1()
  return render(request, 'quiz_question_create.html') 

def store_question(request):
  global QUIZ_COUNT
  qnt = request.POST['question']
  opt1 = request.POST['option1']
  opt2 = request.POST['option2']
  opt3 = request.POST['option3']
  ans = request.POST['answer']
  q = Question(rmdID=str(ID), qnt=qnt, opt1=opt1, opt2=opt2, opt3=opt3, answer=ans)
  q.save()
  QUIZ_COUNT += 1
  
  if QUIZ_COUNT  == 2:
    QUIZ_COUNT = 0
    return render(request, 'quiz_title.html')
  return render(request, 'quiz_question_create.html')

def submition(request):
  title = request.POST['title']

  submit = Quiz(title= title, rm=str(ID))
  submit.save()
  return render(request, 'quiz_completion.html')  

