from django.shortcuts import render
from .models import Hotspot, Event 

# Create your views here.

def home(request):
    return render(request, 'learn/home.html')

def about(request):
    return render(request, 'learn/about.html')

def announcement(request):
    return render(request, 'learn/announcement.html')

def free_wifi(request):
    return render(request, 'learn/free_wifi.html')

def events(request):
    return render(request, 'learn/events.html')

def contact(request):
    return render(request, 'learn/contact.html')

def hotspot_list(request):
    query = request.GET.get('q')  # Get search query from URL
    hotspots = Hotspot.objects.all().order_by('name')
    
    if query:
        hotspots = hotspots.filter(name__icontains=query) 
    
    return render(request, 'learn/hotspot_list.html', {
        'hotspots': hotspots,
        'search_query': query  # Pass query back to template
    })
