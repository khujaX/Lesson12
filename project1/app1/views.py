from django.shortcuts import render
from .models import Site

# Create your views here.

def main_page(request):
    sites = Site.objects.all()
    context = {"sites": sites}
    return render(request, "index.html", context)
