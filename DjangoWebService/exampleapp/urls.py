"""
Definition of urls for DjangoWebService.
"""

from django.conf.urls import url
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^', app.views.api, name='api')
]
