from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse('<h1>welcome to url</h1>') 
def testid(request,id):
    response=f"result avec {id}"
    #response=f"result avec id %s"
    #return HttpResponse(response %id) 
    return HttpResponse(response ,id) 
def renderlist(request):
    list = [
    {
    'title': 'Event 1',
    'description': 'description 1',
    },
    {
    'title': 'Event 2',
    'description': 'description 2',
    },
    {
    'title': 'Event 3',
    'description': 'description 3',
    }
    ]
    return render(request,'events/list.html',{'list':list})
