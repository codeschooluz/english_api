from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Question

@api_view(['GET'])
def home(request):
    data = Question.objects.all()
    lst = []
    for i in data:
        dct = {}
        dct['name'] = i.name
        dct['question'] = i.question
        dct['answer'] = i.answer
        lst.append(dct)
    return Response({'status':'ok', 'data':lst})

@api_view(['GET'])
def get_data(request):
    raw = request.GET
    print(raw)
    data = Question.objects.filter(name=raw.get('name'))
    print(data)
    lst = []
    for i in data:
        dct ={}
        dct['question'] = i.question
        dct['answer'] = i.answer
        lst.append(dct)

    return Response({"data":lst})

@api_view(['POST'])
def put_data(request):
    raw = request.POST
    q = Question(name=raw.get('name'), question=raw.get('question'), answer=raw.get('answer'))
    q.save()
    return Response({'status':'saved'})