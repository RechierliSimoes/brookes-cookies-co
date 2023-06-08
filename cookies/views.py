from django.shortcuts import render
from utils.recipes.factory import make_recipe


def home(request):
    return render(request, 'cookies/pages/home.html', context={
        'cookies': [make_recipe() for _ in range(10)],
    })


def cookie(request, id):
    return render(request, 'cookies/pages/cookies-view.html', context={
        'cookie': make_recipe(),
        'is_detail_page': True,
    })
