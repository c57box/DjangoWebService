"""
Definition of urls for DjangoWebService.
"""

from django.conf.urls import url
import app.views

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^', app.views.api_version, name='api_version')
]
