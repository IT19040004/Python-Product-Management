from django.contrib import admin

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','is_published','create_at')
    list_display_links = ('id','name')
    list_filter = ('price',)
    list_editable = ('is_published',)
    search_fields = ('name','price')
    ordering = ('price',)
    #exclude = ('description',)
    

admin.site.register(Product, ProductAdmin)
