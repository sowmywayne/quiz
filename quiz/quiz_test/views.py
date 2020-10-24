from django.shortcuts import render

# Create your views here.
from home.models import Question
from home.models import Quiz

INDEX = 0
QUESTIONS = {}
SCORE = 0
def index(request):
  global INDEX, SCORE
  INDEX = 0
  SCORE = 0
  return render(request, 'dashboard.html', {'quizes': Quiz.objects.all()})


def view_answer(request):
  return render(request, 'questions.html', {'qnts': QUESTIONS[INDEX - 1], 'ans': QUESTIONS[INDEX-1].answer})



def quize_questions(request):
  global INDEX, QUESTIONS, SCORE

  if INDEX == 0:
    id = request.POST['id']
    QUESTIONS = Question.objects.filter(rmdID=id)
    INDEX += 1
  else:
    
    if request.GET['opt'] == str(QUESTIONS[INDEX - 1].answer):
      SCORE += 10
    if INDEX == 10:
      return render(request, 'score.html', {'score': SCORE})

    INDEX += 1  
    print(SCORE)  
  return render(request, 'questions.html', {'qnts': QUESTIONS[INDEX - 1], 'ans': ""})



          

