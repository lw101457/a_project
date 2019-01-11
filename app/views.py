from django.shortcuts import render

# Create your views here.
from app.models import Lunbo


def index(request):
    lunbo = Lunbo.objects.all()
    lunsli = lunbo[:4]
    lunder = lunbo[4:8]
    lunadd = lunbo[9:]
    lunboslider = {
        'lunsli': lunsli,
        'lunder':lunder,
        'lunadd':lunadd,
    }
    return render(request,'天狗商城.html',context=lunboslider)


# def registere(request):
#     return None
#
#
# def phone(request):
#     return None