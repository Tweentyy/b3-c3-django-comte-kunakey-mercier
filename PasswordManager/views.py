from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SiteForm
from .models import Site
import csv


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

def edit_site(request, id):
    site = get_object_or_404(Site, id=id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SiteForm(instance=site)

    context = {
        "form": form,
        "site": site
    }

    return render(request, 'edit_site.html', context)

def delete_site(request, id):
    site = get_object_or_404(Site, id=id)
    site.delete()

    return redirect('index')

def export_sites(request):
    sites = Site.objects.all()
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="sites.csv"'},
    )

    fieldnames = ['Nom', 'URL', 'Nom d\'utilisateur', 'Mot de passe']
    writer = csv.DictWriter(response, fieldnames=fieldnames)

    writer.writeheader()
    for site in sites:
        writer.writerow(
            {
                'Nom': site.name,
                'URL': site.url,
                'Nom d\'utilisateur': site.username,
                'Mot de passe': site.password
            }
        )

    return response