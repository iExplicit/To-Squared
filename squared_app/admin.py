from django.contrib import admin

# Register your models here.
from .models import Squared, HashTag

admin.site.register(Squared)
admin.site.register(HashTag)
