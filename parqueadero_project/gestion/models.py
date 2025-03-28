# gestion/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_rol

class Usuario(AbstractUser):
    # Usamos email como campo único para login y agregamos el rol.
    email = models.EmailField(unique=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    cedula = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.nombre_cliente

class Vehiculo(models.Model):
    placa = models.CharField(max_length=50, unique=True)
    tipo_vehiculo = models.CharField(max_length=50, blank=True)
    marca = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=50, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vehiculos')

    def __str__(self):
        return self.placa

class Parqueadero(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150, blank=True)
    total_espacios = models.IntegerField()

    def __str__(self):
        return self.nombre

class Tarifa(models.Model):
    descripcion = models.CharField(max_length=100, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_vehiculo = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.descripcion

class Ticket(models.Model):
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='tickets')
    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.CASCADE, related_name='tickets')
    tarifa = models.ForeignKey(Tarifa, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.vehiculo.placa}"

class Factura(models.Model):
    fecha_factura = models.DateTimeField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='factura')

    def __str__(self):
        return f"Factura {self.id}"

class MetodoPago(models.Model):
    nombre_metodo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_metodo

class Recibo(models.Model):
    fecha_recibo = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='recibos', null=True, blank=True)

    def __str__(self):
        return f"Recibo {self.id}"

class Reserva(models.Model):
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.CASCADE, related_name='reservas')

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente.nombre_cliente}"

class Nivel(models.Model):
    nombre_nivel = models.CharField(max_length=50)
    parqueadero = models.ForeignKey(Parqueadero, on_delete=models.CASCADE, related_name='niveles')

    def __str__(self):
        return self.nombre_nivel

class Sector(models.Model):
    nombre_sector = models.CharField(max_length=50)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name='sectores')

    def __str__(self):
        return self.nombre_sector

class Bodega(models.Model):
    descripcion = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='bodegas')

    def __str__(self):
        return self.descripcion

class Historial(models.Model):
    accion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='historiales')

    def __str__(self):
        return f"{self.accion} - {self.usuario.email}"
