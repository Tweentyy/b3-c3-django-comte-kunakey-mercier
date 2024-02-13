from django.shortcuts import render, redirect
from .forms import SiteForm
from .models import Site


def index(request):
    sites = Site.objects.all()
    context = {
        "sites": sites
    }

    return render(request, 'index.html', context)

def add_site(request):
    form = SiteForm()
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form
    }

    return render(request, 'add_site.html', context)