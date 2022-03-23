from django.contrib import admin

# Register your models here.
from listings.models import Band
class BandAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'year_formed', 'genre')
admin.site.register(Band, BandAdmin)

from listings.models import Listing
class ListingAdmin(admin.ModelAdmin):
	list_display = ('id', 'description', 'type_listing', 'band')
admin.site.register(Listing, ListingAdmin)