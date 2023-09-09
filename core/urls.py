# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Add the URL pattern for the test email view
    path('send_test_email/', views.send_test_email, name='send_test_email'),
    # Add other URL patterns as needed
]
