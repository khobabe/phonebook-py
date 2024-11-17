
from django.contrib import admin
from django.urls import path
from contactapp.views import home,delete_contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home-page"),
    path('contact/delete/<int:contact_id>',delete_contact,name="delete-contact")
]
