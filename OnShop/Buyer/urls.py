from django.contrib import admin
from django.urls import path
from Buyer.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index)
]