from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.utils import timezone
from .models import Residencia
from .models import Correspondecia
from .filters import OrderFilter
def index(request):

    correspondencias = Correspondecia.objects.all()
    busqueda = OrderFilter(request.GET, queryset=correspondencias)
    correspondencias = busqueda.qs
    return render(request, 'core/index.html', {'correspondencias': correspondencias.filter(estado='R'), 'busqueda': busqueda})
