from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Board
from .serializers import BoardSerializer



@api_view(['GET'])
def board_list(request):
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)
    print(boards)
    return Response(serializer.data)
