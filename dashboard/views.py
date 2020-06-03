from django.shortcuts import render

# Create your views here.

def dashboards(request):
    return render(request, 'dashboards/index.html', {})