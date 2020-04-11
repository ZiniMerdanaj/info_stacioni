from django.shortcuts import render

from .models import Stacionet, Linjat
# Create your views here.
def index(request):
    context = {}
    return render(request, 'stacionet/index.html', context)

def detail(request, stacion_id):
    stacionet_list = Stacionet.objects.all()
    linjat_list = Linjat.objects.all()
    context = {
        'stacioni': stacion_id,
        'stacionet_list': stacionet_list,
        'linjat_list': linjat_list,
    }
    return render(request, 'stacionet/detail.html', context)