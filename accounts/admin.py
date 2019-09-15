from django.contrib import admin
from .models import accounts
# Register your models here.
admin.site.register(accounts)

admin.site.site_header ="accounts management"