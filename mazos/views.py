from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import ArenaForm
from mazos.models import Tropa, Ejercito, Arena
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def listar_arenas(request):
    arenas = Arena.objects.order_by('nivel')
    return render(request, 'mazos/listar_arenas.html', {'arenas' : arenas})

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

def detalle_arenas(request, pk):
    detalle_arenas = get_object_or_404(Arena, pk=pk)
    return render(request, 'mazos/detalle_arenas.html', {'detalle_arenas': detalle_arenas})

def ejercito_editar(request, pk):
    ejercito = get_object_or_404(Ejercito, pk=pk)
    if request.method == "POST":
        form = ArenaForm(request.POST, instance=post)
        if form.is_valid():
            ejercito = form.save(commit=False)
            ejercito.save()
            return redirect('detalle_arenas', pk=ejercito.arena)
    else:
        form = ArenaForm(instance=post)
    return render(request, 'mazos/mazo_editar.html', {'form': form})

def ejercito_eliminar(request, pk):
    post = get_object_or_404(Ejercito, pk=pk)
    post.delete()
    return redirect('listar_arenas')
