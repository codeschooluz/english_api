from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Question

@api_view(['GET'])
def home(request):
    return Response({'status':'ok'})

@api_view(['GET'])
def get_data(request):
    raw = request.GET
    data = Question.objects.filter(name=raw.get('name'))
    dct = {}
    for i in data:
        dct['question'] = i.question
        dct['answer'] = i.answer

    return Response({"data":data})

@api_view(['POST'])
def put_data(request):
    raw = request.POST
    q = Question(name=raw.get('name'), question=raw.get('question'), answer=raw.get('answer'))
    q.save()
    return Response({'status':'saved'})