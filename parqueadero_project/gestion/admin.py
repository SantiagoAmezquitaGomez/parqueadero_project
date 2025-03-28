# gestion/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (Rol, Usuario, Cliente, Vehiculo, Parqueadero, Tarifa, Ticket,
                     Factura, MetodoPago, Recibo, Reserva, Nivel, Sector, Bodega, Historial)

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'username', 'rol', 'is_staff', 'is_active')
    list_filter = ('rol', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'rol')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'rol', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Rol)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Parqueadero)
admin.site.register(Tarifa)
admin.site.register(Ticket)
admin.site.register(Factura)
admin.site.register(MetodoPago)
admin.site.register(Recibo)
admin.site.register(Reserva)
admin.site.register(Nivel)
admin.site.register(Sector)
admin.site.register(Bodega)
admin.site.register(Historial)
