from django.contrib import admin
from .models import Perro, PersonaInteresada, Adopcion, DetalleAdopcion

@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_raza', 'edad_aproximada', 'estado', 'vacunado')
    list_filter = ('tipo_raza', 'estado', 'vacunado', 'categoria_tamanio')
    search_fields = ('nombre', 'identificador')

@admin.register(PersonaInteresada)
class PersonaInteresadaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'documento', 'email')
    search_fields = ('nombre', 'documento', 'email')

@admin.register(Adopcion)
class AdopcionAdmin(admin.ModelAdmin):
    list_display = ('interesado', 'fecha')
    list_filter = ('fecha',)

@admin.register(DetalleAdopcion)
class DetalleAdopcionAdmin(admin.ModelAdmin):
    list_display = ('perro_adoptado', 'adopcion', 'seguimiento')
    search_fields = ('perro_adoptado__nombre', 'adopcion__interesado__nombre')
