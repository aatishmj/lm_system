from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.signup_info)
admin.site.register(models.ticket)
admin.site.register(models.s_ticket)
admin.site.register(models.h_ticket)