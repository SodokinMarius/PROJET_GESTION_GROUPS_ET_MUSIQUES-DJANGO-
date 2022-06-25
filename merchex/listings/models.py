from django.db import models,migrations
from datetime import datetime
from django.core.validators import MinValueValidator,MaxValueValidator

# CREATION D'UN MODEL
class Band(models.Model):
    name=models.fields.CharField(max_length=100)
    genre=models.fields.CharField(max_length=50)
    biography=models.fields.CharField(max_length=1000)
    year_formed=models.fields.IntegerField(validators=[MinValueValidator(1900),MaxValueValidator(2022)])
    active=models.fields.BooleanField(default=True)
    official_homepage=models.fields.URLField(null=True,blank=True)
 

    #Creation de la classe genre
    class Genre(models.TextChoices):
        HIP_HOP='HH'
        SYNTH_POP='SP'
        ALTERNATIVE_ROCK='AR'
    genre=models.fields.CharField(choices=Genre.choices,max_length=5)

    def __str__(self):
        return f'{self.name}'
    

class Annonce(models.Model):
    title=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=1000)
    sold=models.fields.BooleanField(default=False)
    year=models.fields.IntegerField(null=True,blank=True)
    typeA=models.fields.CharField(max_length=50)

    
    #création de la classe Type
    class Type(models.TextChoices):
        disques='Records'
        vetements='Clothing'
        affiches='Posters'
        divers='Miscellaneous'
    typeA=models.fields.CharField(choices=Type.choices,max_length=50)
    band=models.ForeignKey(Band,null=True,on_delete=models.SET_NULL)


    def __str__(self):
        return f'{self.title}'
    
    

