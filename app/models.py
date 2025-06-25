from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Opciones para los campos de elección
OPCIONES_RAZA = [
    ("CNH", "Caniche"),
    ("CHH", "Chihuahua"),
    ("LBD", "Labrador"),
    ("PTB", "Pitbull"),
    ("MTS", "Mestizo"),
]

OPCIONES_TAMANIO = [
    ("XS", "Extra chico"),
    ("SM", "Chico"),
    ("MD", "Mediano"),
    ("LG", "Grande"),
    ("XL", "Muy grande"),
]

ESTADO_SALUD = [
    ("SAL", "Salud estable"),
    ("OPR", "Operado"),
    ("TRT", "Bajo tratamiento"),
]

SITUACION = [
    ("DISP", "Disponible"),
    ("RESV", "Reservado"),
    ("ADPT", "Adoptado"),
]

CARACTER = [
    ("CLM", "Calmo"),
    ("ACTV", "Activo"),
    ("JGT", "Juguetón"),
    ("PRTC", "Protector"),
]

# Modelo para la mascota
class Perro(models.Model):
    identificador = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_raza = models.CharField(max_length=4, choices=OPCIONES_RAZA)
    edad_aproximada = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(25)])
    categoria_tamanio = models.CharField(max_length=3, choices=OPCIONES_TAMANIO)
    peso_actual = models.DecimalField(max_digits=5, decimal_places=2)
    salud = models.CharField(max_length=3, choices=ESTADO_SALUD)
    vacunado = models.BooleanField(default=False)
    estado = models.CharField(max_length=5, choices=SITUACION, default="DISP")
    comportamiento = models.CharField(max_length=4, choices=CARACTER)

    def modificar_estado(self, nuevo_estado):
        if nuevo_estado in dict(SITUACION):
            self.estado = nuevo_estado
            self.save()

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_raza_display()}) - {self.get_estado_display()}"

# Modelo para personas interesadas en adoptar
class PersonaInteresada(models.Model):
    documento = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    busca_raza = models.CharField(max_length=4, choices=OPCIONES_RAZA, blank=True, null=True)
    busca_tamanio = models.CharField(max_length=3, choices=OPCIONES_TAMANIO, blank=True, null=True)
    busca_caracter = models.CharField(max_length=4, choices=CARACTER, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.documento}"

# Modelo de adopción
class Adopcion(models.Model):
    interesado = models.ForeignKey(PersonaInteresada, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.interesado.nombre} el {self.fecha}"

# Relación entre adopciones y perros
class DetalleAdopcion(models.Model):
    adopcion = models.ForeignKey(Adopcion, on_delete=models.CASCADE)
    perro_adoptado = models.ForeignKey(Perro, on_delete=models.CASCADE)
    seguimiento = models.TextField(blank=True)

    def __str__(self):
        return f"{self.perro_adoptado.nombre} adoptado por {self.adopcion.interesado.nombre}"
