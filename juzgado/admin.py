from django.contrib import admin
from .models import Afectado, Denuncia, Sospechoso, Delincuente, Sospecha

admin.site.register(Afectado)
admin.site.register(Denuncia)
admin.site.register(Sospechoso)
admin.site.register(Delincuente)
admin.site.register(Sospecha)
