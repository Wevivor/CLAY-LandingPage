from django.shortcuts import render, get_object_or_404, redirect
from .models import Email
# Create your views here.


def index(request):

    return render(request, 'index.html')


def complete(request):
    # Email.get_object_or_404()
    # email = Email.objects.all()
    if request.POST:
        email = request.POST['email']
        # email.save()
        return redirect('complete')

    context = {'email': email}

    return render(request, 'complete.html', context)
