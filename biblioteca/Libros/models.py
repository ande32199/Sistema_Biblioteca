from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Reserva(models.Model):
    usuario = models.CharField(max_length=100)  
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()

    def __str__(self):
        return f"Reserva de {self.usuario} - {self.libro.titulo}"

class Usuario(models.Model):  
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

