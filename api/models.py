from django.db import models

# Create your models here.


class Client(models.Model):

    name = models.CharField("Nombre", max_length=255)
    last_name = models.CharField("Apellido", max_length=255)
    email = models.CharField("Email", max_length=255)
    phone = models.IntegerField("Phone")
    is_company = models.BooleanField("Es empresa")

    created = models.DateTimeField("creado", auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Room(models.Model):

    code = models.CharField("Codigo", max_length=255)
    detail = models.TextField("Detalle")

    created = models.DateTimeField("creado", auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class PaymentMethod(models.Model):

    name = models.CharField("Nombre", max_length=255)
    created = models.DateTimeField("creado", auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Invoice(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    name = models.CharField("Nombre", max_length=255)
    detail = models.TextField("Detalle")
    amount_payed = models.IntegerField("Monto Pagado")

    created = models.DateTimeField("creado", auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Booking(models.Model):
    STATE = [
        ("PE", "Pendiente"),
        ("PA", "Pagado"),
        ("DE", "Eliminado"),
    ]

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    date_start = models.DateTimeField("Fecha de Inicio")
    date_end = models.DateTimeField("Fecha de Fin")
    day_stay = models.IntegerField("Dias de Estadia")

    state = models.CharField("Estado", choices=STATE, default="PE", max_length=255)

    created = models.DateTimeField("creado", auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)