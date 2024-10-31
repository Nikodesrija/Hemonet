from django.contrib import admin

# Register your models here.
from .models import BloodBank
from .models import Donor

admin.site.register(BloodBank)
admin.site.register(Donor)