import random
from django.shortcuts import render
from .models import Question
from django.http import JsonResponse

# Start new quiz session
def start_quiz(request):
    request.session['score'] = 0
    request.session['question_count'] = 0
    return JsonResponse({'message': 'Quiz started!'})


# Get a random question
def get_random_question(request):
    question = random.choice(Question.objects.all())
    return JsonResponse({
        'question': question.text,
        'options': [question.option_1, question.option_2, question.option_3, question.option_4],
        'question_id': question.id
    })


# Submit answer and get result
def submit_answer(request):
    question_id = request.POST.get('question_id')
    selected_option = request.POST.get('selected_option')
    question = Question.objects.get(id=question_id)
    
    # Check if the answer is correct
    if selected_option == question.correct_option:
        request.session['score'] += 1

    request.session['question_count'] += 1

    return JsonResponse({
        'score': request.session['score'],
        'total_questions': request.session['question_count'],
        'correct_answer': question.correct_option
    })
