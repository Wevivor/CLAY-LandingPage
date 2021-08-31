from django.shortcuts import render, get_object_or_404, redirect
from .models import Email
# Create your views here.


def index(request):
    if request.GET:
        user = Email()
        user.email = request.GET['user']
        if request.GET['user'] == " ":
            user.email = "no email"
        user.save()
        return redirect("index")
    # if request.POST:
    #     # user=
    #     email = request.POST['user']  # input name= "user"
    #     # email.save()
    #     return redirect('index')
    # # context = {'email': email}
    return render(request, 'index.html')


def complete(request):
    return render(request, 'complete.html')
