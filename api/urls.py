from django.urls import path
from api.views import (
    ClientView,
    ClientCreateView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView,
    RoomView,
    RoomCreateView,
    RoomDetailView,
    RoomUpdateView,
    RoomDeleteView,
    PaymentMethodView,
    PaymentMethodCreateView,
    PaymentMethodDetailView,
    PaymentMethodUpdateView,
    PaymentMethodDelete,
    InvoiceView,
    InvoiceCreateView,
    InvoiceDetailView,
    InvoiceUpdateView,
    InvoiceDeleteView,
    BookingView,
    BookingDetailView,
    BookingUpdateView,
    BookingDeleteView,
    BookingCreateView,
)

urlpatterns = [
    # client
    path("client/", ClientView.as_view(), name="client_all"),
    path("client/create", ClientCreateView.as_view(), name="client_create"),
    path("client/<int:pk>", ClientDetailView.as_view(), name="client_detail"),
    path("client/<int:pk>/update", ClientUpdateView.as_view(), name="client_update"),
    path("client/<int:pk>/delete", ClientDeleteView.as_view(), name="client_delete"),
    # room
    path("room/", RoomView.as_view(), name="room_all"),
    path("room/create", RoomCreateView.as_view(), name="room_create"),
    path("room/<int:pk>", RoomDetailView.as_view(), name="room_detail"),
    path("room/<int:pk>/update", RoomUpdateView.as_view(), name="room_update"),
    path("room/<int:pk>/delete", RoomDeleteView.as_view(), name="room_delete"),
    # payment method
    path("paymentmethod/", PaymentMethodView.as_view(), name="payment_method_all"),
    path("paymentmethod/create", PaymentMethodCreateView.as_view(), name="payment_method_create"),
    path("paymentmethod/<int:pk>", PaymentMethodDetailView.as_view(), name="payment_method_detail"),
    path("paymentmethod/<int:pk>/update", PaymentMethodUpdateView.as_view(), name="payment_method_update"),
    path("paymentmethod/<int:pk>/delete", PaymentMethodDelete.as_view(), name="payment_method_delete"),
    # invoice
    path("invoice/", InvoiceView.as_view(), name="invoice_all"),
    path("invoice/create", InvoiceCreateView.as_view(), name="invoice_create"),
    path("invoice/<int:pk>", InvoiceDetailView.as_view(), name="invoice_detail"),
    path("invoice/<int:pk>/update", InvoiceUpdateView.as_view(), name="invoice_update"),
    path("invoice/<int:pk>/delete", InvoiceDeleteView.as_view(), name="invoice_delete"),
    # booking
    path("booking/", BookingView.as_view(), name="booking_all"),
    path("booking/create", BookingCreateView.as_view(), name="booking_create"),
    path("booking/<int:pk>", BookingDetailView.as_view(), name="booking_detail"),
    path("booking/<int:pk>/update", BookingUpdateView.as_view(), name="booking_update"),
    path("booking/<int:pk>/delete", BookingDeleteView.as_view(), name="booking_delete"),
]
