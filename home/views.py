from django.shortcuts import render
from contracts.models import SmartContract

def home(request):
    context = {
        "contracts":SmartContract.objects.all()
    }
    return render(request,"home/home.html",context)