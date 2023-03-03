from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from .forms import LoginForm,UserRegisterForm


def signIn(req):
    form = LoginForm()
    if req.method == 'GET':
        return render(req,'users/form.html',{'form':form})
    if req.method == 'POST':
        username = req.POST['username']
        pwd = req.POST["passowrd"]
        user = authenticate(req,username=username,password=pwd)
        if user is not None:
            login(request=req,user=user)
            return redirect( 'listeventview' )
        else:
            return render(req,'users/form.html',{'error':'credentials invalid'})
def signup(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/register.html', {'form': form})