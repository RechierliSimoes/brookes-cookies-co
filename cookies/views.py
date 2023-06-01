from django.shortcuts import render


def home(request):
    return render(request, 'cookies/pages/home.html', context={
        'name': 'Rick',
    })
