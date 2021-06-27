from django.shortcuts import render
from contracts.models import SmartContract

def home(request):
    context = {
        "contracts":SmartContract.objects.all().order_by("-created")
    }
    return render(request,"home/home.html",context)