from django.urls import path
from .views import UserRegistrationView, UserConfirmationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('confirm/', UserConfirmationView.as_view(), name='user-confirm'),
]