from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SiteForm

# Create your views here.
@login_required
def add_site(request):
    form = SiteForm()
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('list_sites')
    return render(request, 'add_site.html', {'form': form})