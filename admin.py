from django.contrib import admin
from .models import Toy

class ToyAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'quantity')

admin.site.register(Toy, ToyAdmin)

