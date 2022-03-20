from django.urls import path

from olx.views import api_categories

urlpatterns = [
    path('cats/', api_categories),
]


# 127.0.0.1:8000/olx/api/cats
