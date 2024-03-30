from django.urls import path


from payments.apps import PaymentsConfig
from payments.views import PaymentListAPIView, CreateCheckoutSessionView

app_name = PaymentsConfig.name


urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
]
