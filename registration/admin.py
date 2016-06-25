from django.contrib import admin
from registration.models import registration
# Register your models here.

@admin.register(registration)
class registrationAdmin(admin.ModelAdmin):
	pass