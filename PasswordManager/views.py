from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SiteForm

def index(request):
    return render(request, 'index.html')

def add_site(request):
    form = SiteForm()
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', {'form': form})
    