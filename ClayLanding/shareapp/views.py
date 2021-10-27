from django.shortcuts import render

def share(request):
    return render(request, 'share.html')

def notice(request):
    return render(request,'notice.html')