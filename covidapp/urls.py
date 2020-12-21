from django.contrib import admin
from django.urls import path
from .views import helloworldview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',helloworldview),
]
