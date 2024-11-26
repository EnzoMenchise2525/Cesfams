from django.contrib import admin
from .models import Datos
from .models import Medicamento, ResetaP
# Register your models here.

admin.site.register(Datos)
admin.site.register(Medicamento)
admin.site.register(ResetaP)