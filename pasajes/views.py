from django.shortcuts import render
from .models import Pasajero
from django.views import generic

# Create your views here.

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_pasajeros=Pasajero.objects.all().count()
    

    num_visits=request.session.get('num_visits', 0)
    num_visits=request.session['num_visits']=num_visits+1
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_pasajeros':num_pasajeros, 'num_visits':num_visits},
    )


from django.views import generic

class PasajeroDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Pasajero


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pasajero
class PasajeroCreate(CreateView):
    model = Pasajero
    fields = '__all__'
    initial={'date_of_death':'05/01/2018',}