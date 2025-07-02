from django.contrib import admin

from  .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'price')
    list_editable = ('price',)

admin.site.register(Listing)
