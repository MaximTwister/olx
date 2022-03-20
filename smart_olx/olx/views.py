from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from olx.models import (
    AdvCategory,
)
from olx.serializers import (
    CategorySerializer
)


@api_view(["GET", "POST"])
def api_categories(request):
    if request.method == "GET":
        cats = AdvCategory.objects.all()
        serializer = CategorySerializer(cats, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
