from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Hotspot, Post
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'learn/login.html'

    def form_valid(self, form):
        messages.success(self.request, "Login successful!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin_dashboard')  # Update this to your new adminpanel URL if needed

    def form_invalid(self, form):
        messages.error(self.request, "Invalid credentials!")
        return super().form_invalid(form)

def viewing(request):
    return render(request, 'learn/viewing.html')

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
    query = request.GET.get('q')
    hotspots = Hotspot.objects.all().order_by('name')
    
    if query:
        hotspots = hotspots.filter(name__icontains=query) 
    
    paginator = Paginator(hotspots, 9)  # Show 9 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    total_hotspots = hotspots.count()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('learn/hotspot_list_partial.html', {'page_obj': page_obj})
        return JsonResponse({'html': html})

    return render(request, 'learn/hotspot_list.html', {
        'page_obj': page_obj,
        'search_query': query, # Pass query back to template
        'total_hotspots': total_hotspots,
    })

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registration successful! You can now log in.")
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm() 
    return render(request, 'learn/register.html', {'form': form})

def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'learn/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'learn/post_detail.html', {'post': post})
    
