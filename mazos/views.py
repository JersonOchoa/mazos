from django.shortcuts import render
from django.contrib import messages
from .forms import ArenaForm
from mazos.models import Tropa, Ejercito, Arena

def ejercito_nuevo(request):

    if request.method == "POST":

        formulario = ArenaForm(request.POST)

        if formulario.is_valid():

            arena = Arena.objects.create(nombre=formulario.cleaned_data['nombre'], nivel = formulario.cleaned_data['nivel'])

            for tropa_id in request.POST.getlist('tropas'):

                ejercito = Ejercito(tropa_id=tropa_id, arena_id = arena.id)

                ejercito.save()

            messages.add_message(request, messages.SUCCESS, 'Ejercito guardado Exitosamente!')

    else:

        formulario = ArenaForm()

    return render(request, 'mazos/mazo_editar.html', {'formulario': formulario})
