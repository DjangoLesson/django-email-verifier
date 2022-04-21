from django.urls import path
from . import views


urlpatterns = [
    path('login/', view=views.LoginView.as_view(), name='login'),
    path('register/', view=views.RegistrationView.as_view(), name='register'),
    path('token/<str:token>', view=views.TokenView.as_view(), name='verify-token'),
]
