from django.urls import path
from .views import *

urlpatterns = [
    path('',Dashboard,name='dash'),
    path('add_e',addEmployee,name='add_e'),
    path('edit_e /<int:id>/',EditEmp,name='edit_e'),
    path('delete_e /<int:id>/',DeleteEmp,name='delete_e')
]
