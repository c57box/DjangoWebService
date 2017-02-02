"""
Definition of APIs.
"""
import json
from django.http import HttpRequest
from django.http import HttpResponse
import numpy as np

def generate_data():
    """ 
    private function 
    return a json array like below,
    [
        {"1" : 8.0}
        {"2" : 6.0}
        ...
        {"17": 9.9}
    ]
    index >= 8 < 18
    """
    data = np.random.randn(8 + np.random.randint(10)) * 100
    chart_data = []
    for index, val in enumerate(data):
        chart_data.append({str(index) : val})
    return chart_data

def api(request):
    """ django api function """
    assert isinstance(request, HttpRequest)

    if request.method == "GET":
        data = json.dumps(generate_data())
        return HttpResponse(data, content_type='application/json')
