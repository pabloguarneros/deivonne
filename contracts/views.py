from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import SmartContract
from .forms import SmartContractForm


def addContract(request):
    #if not request.user.is_authenticated:
        #return HttpResponseRedirect(reverse("login"))
    context={
        'form': SmartContractForm()
    }
    return render(request, 'contracts/createContract.html',context)


def addHash(request):

    if request.method == "POST":
        form = SmartContractForm(request.POST,request.FILES)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            short_description = form.cleaned_data.get('short_description')
            sector = form.cleaned_data.get('sector')
            hash = form.cleaned_data.get('hash')
            contract = SmartContract.objects.create(title=title,short_description=short_description,sector=sector,hash=hash)
            contract.save()
            poster = form.cleaned_data['poster']
            contract.poster = poster
            contract.save()

        return HttpResponseRedirect("/")
