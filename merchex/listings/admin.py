from django.contrib import admin
from listings.models import Band
from listings.models import Annonce

class BandAdmin(admin.ModelAdmin):
    list_display=('name','year_formed','genre','biography')
class ListingsAdmin(admin.ModelAdmin):
    list_display=('title','description','sold','year','band','id')

admin.site.register(Band,BandAdmin)

admin.site.register(Annonce,ListingsAdmin)

# Register your models here.
