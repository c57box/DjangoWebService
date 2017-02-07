"""
Definition of APIs.
"""
import sys
import json
from django.http import HttpRequest
from django.http import HttpResponse
from django.conf import settings

def api_version(request):
    """ A django web api example without model"""
    assert isinstance(request, HttpRequest)

    if request.method == "GET":
        if settings.API_VERSION == {}:
            settings.API_VERSION = {"MyApiVersion" : "v1.0"}

        return HttpResponse(
            json.dumps(settings.API_VERSION),
            status=200,
            content_type='application/json')

    if request.method == "POST":
        try:
            json_data = json.loads(request.body.decode('utf-8'))

            log = 'My API Version Number changed from %s to %s' % (
                settings.API_VERSION['MyApiVersion'],
                json_data['MyApiVersion'])
            print(log)

            settings.API_VERSION = json_data

            return HttpResponse(status=200)
        except:
            e = sys.exc_info()[0]
            print('TestPost failed. %s' % (e))
            return HttpResponse(status=400)

    if request.method == "PUT":
        pass
    if request.method == "PATCH":
        pass
    if request.method == "DELETE":
        pass
