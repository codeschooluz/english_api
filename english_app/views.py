from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Question

@api_view(['GET'])
def get_data(request):
    raw = request.GET
    data = Question.objects.filter(name=raw.get('name'))
    dct = {}
    for i in data:
        dct['question'] = i.question
        dct['answer'] = i.answer

    return Response({"data":data})