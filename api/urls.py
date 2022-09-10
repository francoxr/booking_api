from django.urls import path
from api.views import (
    BookingView,
    BookingDetailView,
    ClientView,
    ClientDetailView,
    PaymentMethodView,
    PaymentMethodDetailView,
    RoomView,
    RoomDetailView,
    InvoiceView,
    InvoiceDetailView,
)

urlpatterns = [
    path("booking/", BookingView.as_view(), name="booking_all"),
    path("booking/<int:pk>", BookingDetailView.as_view(), name="booking_detail"),
    path("client/", ClientView.as_view(), name="client_all"),
    path("client/<int:pk>", ClientDetailView.as_view(), name="client_detail"),
    path("room/", RoomView.as_view(), name="client_all"),
    path("room/<int:pk>", RoomDetailView.as_view(), name="client_detail"),
    path("paymentmethod/", PaymentMethodView.as_view(), name="payment_method_all"),
    path("paymentmethod/<int:pk>", PaymentMethodDetailView.as_view(), name="payment_method_detail"),
    path("invoice/", InvoiceView.as_view(), name="invoice_all"),
    path("invoice/<int:pk>", InvoiceDetailView.as_view(), name="invoice_detail"),
]
