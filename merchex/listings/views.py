from django.http import HttpResponse
from django.shortcuts import render,redirect
from listings.models import Band
from listings.models import Annonce
from listings.forms import ContactUsForm,BandForm,ListingForm
from django.core.mail import send_mail

#Module de Redirection de Mesage
from django.shortcuts import redirect

def band_list(request):
    bands=Band.objects.all()
    return render(request,'listings/band_list.html',
    {'first_band':bands})

def annonce_list(request):
    annonces=Annonce.objects.all()
    return render(request,'listings/annonce_list.html',
    {'listings':annonces})

def about(request):
    contenu='A propos. Nous adorons merch. Espert !!!'
    return render(request,'listings/about.html',
    {'contenu':contenu})


#Ici nous avons renvoyer l'objet form
def contact(request):
    if request.method=='POST':
        #creation d'une instance du formulaire et le remplir
        form=ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us Form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['yaomariussodokin@gmail.com']
            )
            #Redirection
            return redirect('email-sent')

    else:
        #creation d'une instance de formulaire vide
        form=ContactUsForm()
    
    return render(request,'listings/contact.html',
    {'form': form})


#Vue pour la page des details
def band_detail(request,id):
    band=Band.objects.get(id=id)
    return render(request,
    'listings/band_detail.html',
    {'band':band})


def band_create(request):
    if request.method=='POST':
        form=BandForm(request.POST)

        #Verification de la validation des valeurs
        if form.is_valid():
            band=form.save()

            #redirection
            return redirect('band-detail',band.id)
    
    else:
        form=BandForm()

    return render(request,
        'listings/band_create.html',
        {'form':form})

#Vue d'Enregistrement d'une annonce
def annonce_create(request):
    if request.method=='POST':
        form=ListingForm(request.POST)
        
        if form.is_valid():
            annonce=form.save()

            #redirection
            return redirect('annonce-create',annonce.id)
    else:
        form=ListingForm()

    return render(request,
    'listings/annonce_create.html',
    {'form':form})


def annonce_detail(request,id):
    annonce=Annonce.objects.get(id=id)
    return render(request,
    'listings/annonce_detail.html',
    {'annonce':annonce})

#Vue pour la page de confirmation
def confirmation(request):
    return render(request,
    'listings/email_sent.html',
    {'confirmation': "Veuillez confirmer le nouvel envoi du formulaire !!!"})


#Mise à jour d'un groupe 
def update_band(request,id):
    band=Band.objects.get(id=id)

    if request.method=='POST':
        form=BandForm(request.POST,instance=band)
        if form.is_valid():
            form.save()

            return redirect('band-detail',band.id)
    else:
        #remplir le formulaire
        form=BandForm(instance=band)

    return render(request,
    'listings/band_update.html',
    {'form':form})


    #Mettre à jour une annonce
def update_annonce(request,id):
    annonce=Annonce.objects.get(id=id)

    if request.method=='POST':
        form=ListingForm(request.POST,instance=annonce)
        if form.is_valid():
            form.save()

            #redirection
            return redirect('annonce-detail',annonce.id)
    else:
        form=ListingForm(instance=annonce)
    
    return render(request,
                'listings/annonce_update.html',
                {'form':form})

#Vue de suppression
def delete_band(request,id):
    band=Band.objects.get(id=id)
    
    if request.method=='POST':
        band.delete()

        return redirect('band-list')
    return render(request,
    'listings/band_delete.html',
    {'band':band})


def delete_annonce(request,id):
    annonce=Annonce.objects.get(id=id)
    
    if request.method=='POST':
        annonce.delete()

        return redirect('annonce-list')
    return render(request,
    'listings/annonce_delete.html',
    {'annonce':annonce})