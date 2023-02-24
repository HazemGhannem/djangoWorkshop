from django.shortcuts import render
from django.http import HttpResponse
from .models import Events
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import *
from django.shortcuts import redirect
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

def ListEven(request):
    #list=Events.objects.all()
    list=Events.objects.filter(state=True)# filter with state
    return render(request,'events/list.html',{'list':list})
class ListEvent(ListView):
    model = Events
    template_name='events/list.html'
    context_object_name="list"
    #paginate_by = 10
    def get_queryset(self) :
        return Events.objects.filter(state=False)

class DetailEventView(DetailView):
    model= Events
    template_name='events/detailEvent.html'
    context_object_name="list"
    #slug_field = 'title'

def add_event(req):
    form =EventForm() 
    print("test")
    if req.method =='POST':
        form= EventForm(req.POST,req.FILES)  
        print("test")
        if form.is_valid():
            print(form)
            #print(**form.cleaned_data)
            Events.objects.create(**form.cleaned_data)
            print("test")
            return redirect( 'listeventview' )
        else:
            print(form.errors)
            print("test")
    return render(req,"events/event.html",{'form': form})
