from django.shortcuts import render

def index(request):
    context = {
        'title': 'Search'
    }
    return render(request, 'reports/index.html', context=context)

def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'reports/about.html', context=context)
