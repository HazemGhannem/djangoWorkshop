from django.shortcuts import render
from django.http import HttpResponse
from .models import Events
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import EventForm
from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



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
class ListEvent(LoginRequiredMixin,ListView):
    login_url='login'
    model = Events
    template_name='events/list.html'
    context_object_name="list"
    #paginate_by = 10
    def get_queryset(self) :
        return Events.objects.filter(state=False)

class DetailEventView(LoginRequiredMixin,DetailView):
    login_url='login'
    model= Events
    template_name='events/detailEvent.html'
    context_object_name="list"
    #slug_field = 'title'

class UpdateView(LoginRequiredMixin,UpdateView):
    login_url='login'
    model= Events
    form_class=EventForm
    template_name='events/event.html'
    
class DeleteView(LoginRequiredMixin,DeleteView):
    login_url='login'
    model= Events
    template_name = "events/deleteevent.html"
    success_url=reverse_lazy('listeventview')

  
@login_required(login_url='login')
def add_event(req):
    form =EventForm() 
    if req.method =='POST':
        form= EventForm(req.POST,req.FILES)  
        if form.is_valid():
            print(form)
            #print(**form.cleaned_data)
            Events.objects.create(**form.cleaned_data)
            return redirect( 'listeventview' )
        else:
            print(form.errors)
    return render(req,"events/event.html",{'form': form})



def parti(req,pk):
    current_user = req.user
    curren_event=Events.objects.filter(pk=pk)
    event=Events.objects.filter(Participation=current_user)
    for i in curren_event:
        print(i.nbe_participan- i.Participation.count()>0)
        if (i.nbe_participan- i.Participation.count()>0):
            i.Participation.add(current_user)
            i.save()
    return render(req,"events/parti.html",{'list': event})