from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ClassicCafeFeedbackModel
from django.core.exceptions import ValidationError
from .serializers import UserFeedbackSerializer
from django.http import HttpRequest, JsonResponse
import json

# Create your views here.
@api_view(['GET'])
def get_user_feedback(request):
    if request.method == 'GET':
        feeds = ClassicCafeFeedbackModel.objects.all()
        serializer = UserFeedbackSerializer(feeds, many=True)
        return Response({'status': True, 'data': serializer.data})
    else:
        response_data = {'status': False, 'message': 'Method Not Allowed.'}
        return Response(response_data, status=405)

def get_rate_value(rate):
    for i, a in dict(ClassicCafeFeedbackModel.status_choice.choices).items():
        if a == rate:
            return i
    
def has_verified_rate(rate):
    for a in dict(ClassicCafeFeedbackModel.status_choice.choices).values():
        if a == rate:
            return True
    return False

@csrf_exempt
@require_POST
def feedback_api(request:HttpRequest):
    # Validasyon gamit ang Django Form o Django's input validation ay inirerekomenda para sa mas malinis na code.
    data = json.loads(request.body)
    name = data['name']
    feed = data['feedback']
    rate = data['rate']
    if not name:
        response_data = {'status': False, 'message': 'Invalid name.'}
        return JsonResponse(response_data, status=400)

    if not feed:
        response_data = {'status': False, 'message': 'Invalid feedback.'}
        return JsonResponse(response_data, status=400)

    if not has_verified_rate(rate):
        response_data = {'status': False, 'message': 'Invalid rate choice.'}
        return JsonResponse(response_data, status=400)

    rate_value = get_rate_value(rate)  # Kumuha ng value ng rate
    try:
        ClassicCafeFeedbackModel.objects.create(name=name, feedback=feed, rate=rate_value)
        response_data = {'status': True, 'message': 'Feedback received successfully.'}
        return JsonResponse(response_data)
    except ValidationError as e:
        response_data = {'status': False, 'message': str(e)}  # Maaring customized error message depende sa validation
        return JsonResponse(response_data, status=400)
    except Exception as e:
        response_data = {'status': False, 'message': 'An error occurred while saving the feedback.'}
        return JsonResponse(response_data, status=500)