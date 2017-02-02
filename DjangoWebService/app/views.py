"""
Definition of APIs.
"""
import json
from django.http import HttpRequest
from django.http import HttpResponse

def myapi(request, *args, **kwargs):
    """ a django web api example without model"""
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if len(args) == 0:
            data = json.dumps({"My Api version" : "v1.0"})
            return HttpResponse(data, content_type='application/json')
        else:
            pass

    if request.method == "POST":
        if len(kwargs) == 0:
            return HttpResponse(status=400)
        else:
            pass

    if request.method == "PUT":
        try:
            id = int(args[0])
            pass
        except ValueError:
            return HttpResponse(status=400)
        if len(kwargs) == 0:
            return HttpResponse(status=400)
        else:
            pass

    if request.method == "PATCH":
        try:
            id = int(args[0])
            pass
        except ValueError:
            return HttpResponse(status=404)
        if len(kwargs) == 0:
            return HttpResponse(status=404)
        else:
            pass

    if request.method == "DELETE":
        try:
            id = int(args[0])
            pass
        except ValueError:
            return HttpResponse(status=400)
