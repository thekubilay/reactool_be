from users.views import login
from django.urls import path

urlpatterns = [
	path('', login, name='login'),
]
