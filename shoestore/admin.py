from django.contrib import admin

from shoestore.models import Size,Category,Brand,Tag,Material,Season,Product

# Register your models here.
admin.site.register(Size)

admin.site.register(Category)

admin.site.register(Brand)

admin.site.register(Tag)

admin.site.register(Material)

admin.site.register(Season)

admin.site.register(Product)

