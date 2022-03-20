from django.urls import path
from django.urls import include

urlpatterns = [
    path('olx/api/', include("olx.urls")),
]

# 127.0.0.1:8000/olx/api/
