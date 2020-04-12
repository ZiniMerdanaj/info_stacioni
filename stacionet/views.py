from django.shortcuts import render, redirect

from .models import Stacionet, Linjat
from .forms import StacionIdForm
# Create your views here.
def index(request):
    if request.method =='POST':
        form = StacionIdForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['stacion_id']
            print(id)
            return redirect('%s/' % id)
    else:
        form = StacionIdForm()

    context = {'form': form}
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