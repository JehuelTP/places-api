from django.db import models
from accounts.models import User


class Lugar(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    provincia = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)

    ubicacion = models.CharField(max_length=300)

    latitud = models.DecimalField(max_digits=10, decimal_places=7)
    longitud = models.DecimalField(max_digits=10, decimal_places=7)

    url = models.URLField(max_length=500, blank=True, null=True)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Horario(models.Model):
    DIAS = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
        ('SAB', 'Sábado'),
        ('DOM', 'Domingo'),
    ]

    lugar = models.ForeignKey(
        Lugar,
        on_delete=models.CASCADE,
        related_name='horarios'
    )

    dia = models.CharField(max_length=3, choices=DIAS)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.lugar.nombre} - {self.dia}"


class Foto(models.Model):
    lugar = models.ForeignKey(
        Lugar,
        on_delete=models.CASCADE,
        related_name='fotos'
    )

    url_imagen = models.URLField(max_length=500)
    descripcion = models.CharField(max_length=500, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion or f"Foto {self.id}"


class ComentarioLugar(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comentarios_lugares'
    )

    lugar = models.ForeignKey(
        Lugar,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )

    comentario = models.TextField()
    calificacion = models.PositiveSmallIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    comentario_padre = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='respuestas'
    )

    def __str__(self):
        return f"{self.usuario} - {self.lugar}"


class Favorito(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favoritos_lugares'
    )

    lugar = models.ForeignKey(
        Lugar,
        on_delete=models.CASCADE,
        related_name='favoritos'
    )

    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'lugar')

    def __str__(self):
        return f"{self.usuario} -> {self.lugar}"