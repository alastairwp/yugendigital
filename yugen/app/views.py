from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from django.shortcuts import render


# Create your views here.
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home | Yugen Digital',
            'year': datetime.now().year,
        }
    )
