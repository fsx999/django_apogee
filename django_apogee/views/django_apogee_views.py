from __future__ import unicode_literals
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django_apogee.models import AnneeUni
from django_apogee.serializers.models_apogee_serializers import AnneeUniSerializer

__author__ = 'juggernut'


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def anneuni_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        annees = AnneeUni.objects.all()
        serializer = AnneeUniSerializer(annees, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AnneeUniSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

