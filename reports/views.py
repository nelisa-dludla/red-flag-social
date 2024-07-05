from django.shortcuts import render

def index(request):
    return render(request, 'reports/index.html')

def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'reports/about.html', context=context)
