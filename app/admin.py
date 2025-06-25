from django.contrib import admin
from .models import Perro, PersonaInteresada, Adopcion, DetalleAdopcion

@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ("identificador", "nombre", "tipo_raza", "edad_aproximada", "categoria_tamanio", "vacunado", "estado")
    list_filter = ("tipo_raza", "categoria_tamanio", "estado", "vacunado")
    search_fields = ("nombre", "identificador")

@admin.register(PersonaInteresada)
class PersonaInteresadaAdmin(admin.ModelAdmin):
    list_display = ("documento", "nombre", "email")
    search_fields = ("nombre", "documento", "email")

@admin.register(Adopcion)
class AdopcionAdmin(admin.ModelAdmin):
    list_display = ("interesado", "fecha")
    list_filter = ("fecha",)

@admin.register(DetalleAdopcion)
class DetalleAdopcionAdmin(admin.ModelAdmin):
    list_display = ("get_perro", "get_interesado", "adopcion", "seguimiento_post_adopcion")
    search_fields = ("adopcion__interesado__nombre", "perro__nombre")

    def get_perro(self, obj):
        return obj.perro.nombre
    get_perro.short_description = "Perro"

    def get_interesado(self, obj):
        return obj.adopcion.interesado.nombre
    get_interesado.short_description = "Adoptante"










