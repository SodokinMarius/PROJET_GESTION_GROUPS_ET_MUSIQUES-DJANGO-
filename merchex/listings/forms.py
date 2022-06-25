from django import forms
from listings.models import Band,Annonce

class ContactUsForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
    class Meta:
        model=Band
        #fields='__all__'
        exclude=('active','official_homepage')

class ListingForm(forms.ModelForm):
    class Meta:
        model=Annonce
        fields='__all__'