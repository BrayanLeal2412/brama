from django.urls import path
from . import views

urlpatterns = [
   path ('', views.index, name='index'),
   path('pasajeros/<int:pk>', views.PasajeroDetailView.as_view(), name='pasajero-detail')
]

urlpatterns += [
    path('pasajero/crear/', views.PasajeroCreate.as_view(), name='pasajero_create'),
    
]