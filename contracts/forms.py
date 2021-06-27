from django import forms
from .models import SmartContract


class SmartContractForm(forms.ModelForm):
    
    hash = forms.CharField(
            label="Smart Contract's Hash",
            help_text="It should start with 'KT1'",
        )
    short_description = forms.CharField(
            label="Short Description",
            help_text="Describe what your Smart Contract's function does in the backend and what is it for",
        )
    sector = forms.ChoiceField(
            label="Industry Affected"
        )
    poster = forms.ImageField(label="Contract's Profile Image")


    class Meta:
        model=SmartContract
        fields=['title','short_description','hash','poster','sector']
