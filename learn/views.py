from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'learn/home.html')

def about(request):
    return render(request, 'learn/about.html')

def announcement(request):
    return render(request, 'learn/announcement.html')

def free_wifi(request):
    return render(request, 'learn/contact.html')

def events(request):
    return render(request, 'learn/events.html')

def contact(request):
    return render(request, 'learn/contact.html')
