from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Booking, Client, PaymentMethod, Room, Invoice
from api.serializers import ClientSerializer, RoomSerializer, PaymentMethodSerializer, BookingSerializer, InvoiceSerializer

# ------ Client -------
class ClientView(APIView):

    # list
    def get(self, request):
        clients = Client.objects.all()
        if clients:
            clients_serializers = ClientSerializer(clients, many=True)
            return Response(clients_serializers.data, status=status.HTTP_200_OK)
        return Response({"message": "No existen Clientes"}, status=status.HTTP_400_BAD_REQUEST)

    # create
    def post(self, request):
        clients_serializers = ClientSerializer(data=request.data)
        if clients_serializers.is_valid():
            clients_serializers.save()
            return Response({"message": "Cliente Creado Correctamente"}, status=status.HTTP_201_CREATED)
        return Response(clients_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailView(APIView):

    # retrieve
    def get(self, request, pk):
        client = Client.objects.filter(id=pk).first()
        if client:
            client_serializer = ClientSerializer(client)
            return Response(client_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Cliente No existe"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        client = Client.objects.filter(id=pk).first()
        if client:
            client_serializer = ClientSerializer(client, data=request.data, partial=True)
            if client_serializer.is_valid():
                client_serializer.save()
                return Response(client_serializer.data, status=status.HTTP_200_OK)
            return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Cliente No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # update
    def put(self, request, pk):
        client = Client.objects.filter(id=pk).first()
        if client:
            client_serializer = ClientSerializer(client, data=request.data)
            if client_serializer.is_valid():
                client_serializer.save()
                return Response(client_serializer.data, status=status.HTTP_200_OK)
            return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Cliente No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        client = Client.objects.filter(id=pk).first()
        if client:
            client.delete()
            return Response({"message": "Cliente Eliminado Correctamente"}, status=status.HTTP_200_OK)
        return Response({"message": "Cliente No existe"}, status=status.HTTP_400_BAD_REQUEST)


# ------ Room -------
class RoomView(APIView):

    # list
    def get(self, request):
        rooms = Room.objects.all()
        if rooms:
            rooms_serializers = RoomSerializer(rooms, many=True)
            return Response(rooms_serializers.data, status=status.HTTP_200_OK)
        return Response({"message": "No existen Cuartos"}, status=status.HTTP_400_BAD_REQUEST)

    # create
    def post(self, request):
        rooms_serializers = RoomSerializer(data=request.data)
        if rooms_serializers.is_valid():
            rooms_serializers.save()
            return Response({"message": "Cuarto Creado Correctamente"}, status=status.HTTP_201_CREATED)
        return Response(rooms_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailView(APIView):

    # retrieve
    def get(self, request, pk):
        room = Room.objects.filter(id=pk).first()
        if room:
            room_serializer = RoomSerializer(room)
            return Response(room_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Cuarto No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # update
    def patch(self, request, pk):
        room = Room.objects.filter(id=pk).first()
        if room:
            room_serializer = RoomSerializer(room, data=request.data, partial=True)
            if room_serializer.is_valid():
                room_serializer.save()
                return Response(room_serializer.data, status=status.HTTP_200_OK)
            return Response(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Cuarto No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # update
    def put(self, request, pk):
        room = Room.objects.filter(id=pk).first()
        if room:
            room_serializer = RoomSerializer(room, data=request.data)
            if room_serializer.is_valid():
                room_serializer.save()
                return Response(room_serializer.data, status=status.HTTP_200_OK)
            return Response(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Cuarto No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        room = Room.objects.filter(id=pk).first()
        if room:
            room.delete()
            return Response({"message": "Cuarto Eliminado Correctamente"}, status=status.HTTP_200_OK)
        return Response({"message": "Cuarto No existe"}, status=status.HTTP_400_BAD_REQUEST)


# ------ Payment Method -------
class PaymentMethodView(APIView):

    # list
    def get(self, request):
        payment_method = PaymentMethod.objects.all()
        if payment_method:
            payment_method_serializers = PaymentMethodSerializer(payment_method, many=True)
            return Response(payment_method_serializers.data, status=status.HTTP_200_OK)
        return Response({"message": "No existen Metodos de Pago"}, status=status.HTTP_400_BAD_REQUEST)

    # create
    def post(self, request):
        payment_method_serializers = PaymentMethodSerializer(data=request.data)
        if payment_method_serializers.is_valid():
            payment_method_serializers.save()
            return Response({"message": "Metodo de Pago Creado Correctamente"}, status=status.HTTP_201_CREATED)
        return Response(payment_method_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentMethodDetailView(APIView):

    # retrieve
    def get(self, request, pk):
        payment_method = PaymentMethod.objects.filter(id=pk).first()
        if payment_method:
            payment_method_serializer = PaymentMethodSerializer(payment_method)
            return Response(payment_method_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Metodo de Pago No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # update
    def patch(self, request, pk):
        payment_method = PaymentMethod.objects.filter(id=pk).first()
        if payment_method:
            payment_method_serializer = PaymentMethodSerializer(payment_method, data=request.data, partial=True)
            if payment_method_serializer.is_valid():
                payment_method_serializer.save()
                return Response(payment_method_serializer.data, status=status.HTTP_200_OK)
            return Response(payment_method_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Metodo de Pago No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # update
    def put(self, request, pk):
        payment_method = PaymentMethod.objects.filter(id=pk).first()
        if payment_method:
            payment_method_serializer = PaymentMethodSerializer(payment_method, data=request.data)
            if payment_method_serializer.is_valid():
                payment_method_serializer.save()
                return Response(payment_method_serializer.data, status=status.HTTP_200_OK)
            return Response(payment_method_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Metodo de Pago No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        payment_method = PaymentMethod.objects.filter(id=pk).first()
        if payment_method:
            payment_method.delete()
            return Response({"message": "Metodo de Pago Eliminado Correctamente"}, status=status.HTTP_200_OK)
        return Response({"message": "Metodo de Pago No existe"}, status=status.HTTP_400_BAD_REQUEST)


# ------ Invoice -------
class InvoiceView(APIView):

    # list
    def get(self, request):
        invoice = Invoice.objects.all()
        if invoice:
            invoice_serializers = InvoiceSerializer(invoice, many=True)
            return Response(invoice_serializers.data, status=status.HTTP_200_OK)
        return Response({"message": "No existen Facturas"}, status=status.HTTP_400_BAD_REQUEST)

    # create
    def post(self, request):
        invoice_serializers = InvoiceSerializer(data=request.data)
        if invoice_serializers.is_valid():
            invoice_serializers.save()
            return Response({"message": "Factura Creado Correctamente"}, status=status.HTTP_201_CREATED)
        return Response(invoice_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class InvoiceDetailView(APIView):

    # retrieve
    def get(self, request, pk):
        invoice = Invoice.objects.filter(id=pk).first()
        if invoice:
            invoice_serializer = InvoiceSerializer(invoice)
            return Response(invoice_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Factura No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # update
    def patch(self, request, pk):
        invoice = Invoice.objects.filter(id=pk).first()
        if invoice:
            invoice_serializer = InvoiceSerializer(invoice, data=request.data, partial=True)
            if invoice_serializer.is_valid():
                invoice_serializer.save()
                return Response(invoice_serializer.data, status=status.HTTP_200_OK)
            return Response(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Factura No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # update
    def put(self, request, pk):
        invoice = Invoice.objects.filter(id=pk).first()
        if invoice:
            invoice_serializer = InvoiceSerializer(invoice, data=request.data)
            if invoice_serializer.is_valid():
                invoice_serializer.save()
                return Response(invoice_serializer.data, status=status.HTTP_200_OK)
            return Response(invoice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Factura No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        invoice = Invoice.objects.filter(id=pk).first()
        if invoice:
            invoice.delete()
            return Response({"message": "Factura Eliminado Correctamente"}, status=status.HTTP_200_OK)
        return Response({"message": "Factura No existe"}, status=status.HTTP_400_BAD_REQUEST)


# ------ Booking -------
class BookingView(APIView):

    # list
    def get(self, request):
        bookings = Booking.objects.all()
        if bookings:
            bookings_serializers = BookingSerializer(bookings, many=True)
            return Response(bookings_serializers.data, status=status.HTTP_200_OK)
        return Response({"message": "No existen Reservaciones"}, status=status.HTTP_400_BAD_REQUEST)

    # create
    def post(self, request):
        booking_serializer = BookingSerializer(data=request.data)
        if booking_serializer.is_valid():
            booking_serializer.save()
            return Response({"message": "Reservacion Creado Correctamente"}, status=status.HTTP_201_CREATED)
        return Response(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDetailView(APIView):

    # retrieve
    def get(self, request, pk):
        booking = Booking.objects.filter(id=pk).first()
        if booking:
            booking_serializer = BookingSerializer(booking)
            return Response(booking_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Reservacion No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # update
    def patch(self, request, pk):
        booking = Booking.objects.filter(id=pk).first()
        if booking:
            booking_serializer = BookingSerializer(booking, data=request.data, partial=True)
            if booking_serializer.is_valid():
                booking_serializer.save()
                return Response(booking_serializer.data, status=status.HTTP_200_OK)
            return Response(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Reservacion No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # update
    def put(self, request, pk):
        booking = Booking.objects.filter(id=pk).first()
        if booking:
            booking_serializer = BookingSerializer(booking, data=request.data)
            if booking_serializer.is_valid():
                booking_serializer.save()
                return Response(booking_serializer.data, status=status.HTTP_200_OK)
            return Response(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Reservacion No existe"}, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        booking = Booking.objects.filter(id=pk).first()
        if booking:
            booking.delete()
            return Response({"message": "Reservacion Eliminado Correctamente"}, status=status.HTTP_200_OK)
        return Response({"message": "Reservacion No existe"}, status=status.HTTP_400_BAD_REQUEST)
