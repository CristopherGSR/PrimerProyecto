from django.shortcuts import render
#from django.http import HttpResponse
#def home(request):
#    return HttpResponse('Hello, World!')
from wsgiref.util import request_uri
from django.http import HttpResponse
from .models import Board
def home(request):

    boards = Board.objects.all()
    return render(request, 'home.html',{'boards': boards})
    #boards = Board.objects.all()
    #boards_names = list()
    #for board in boards:
    #    boards_names.append(board.name)
    #response_html = '<br>'.join(boards_names)
    #return HttpResponse(response_html)
# Create your views here.
