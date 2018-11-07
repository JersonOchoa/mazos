from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib import messages
from .forms import ArenaForm
from mazos.models import Tropa, Ejercito, Arena
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.db.models import Q

def listar_arenas(request):
    arenas = Arena.objects.order_by('nivel')
    return render(request, 'mazos/listar_arenas.html', {'arenas' : arenas})

@login_required
def ejercito_nuevo(request):

    if request.method == "POST":
        form = ArenaForm(request.POST)
        if form.is_valid():
            arena = Arena.objects.create(nombre=form.cleaned_data['nombre'], nivel = form.cleaned_data['nivel'])
            for tropa_id in request.POST.getlist('tropas'):
                ejercito = Ejercito(tropa_id=tropa_id, arena_id = arena.id)
                ejercito.save()

            messages.add_message(request, messages.SUCCESS, 'Ejercito guardado Exitosamente!')

    else:

        form = ArenaForm()

    return render(request, 'mazos/mazo_editar.html', {'form': form})

def detalle_arenas(request, pk):

    detalle_arenas = get_list_or_404(Ejercito.objects.order_by('arena'), arena=pk) #get_object_or_404(Ejercito, pk=pk)
    return render(request, 'mazos/detalle_arenas.html', {'detalle_arenas': detalle_arenas})

@login_required
def ejercito_editar(request, pk):
    arena = get_object_or_404(Arena, pk=pk)
    if request.method == "POST":
        form = ArenaForm(request.POST, instance=arena)
        if form.is_valid():
            for tropa_id in request.POST.getlist('tropas'):
                ejercito = Ejercito(tropa_id=tropa_id, arena_id=arena.id)
                ejercito.save()
            arena = form.save(commit=False)
            arena.save()
            return redirect('detalle_arenas', pk=arena.pk)
    else:
        form = ArenaForm(instance=arena)
    return render(request, 'mazos/mazo_editar.html', {'form': form})

@login_required
def ejercito_eliminar(request, pk):
    post = get_object_or_404(Arena, pk=pk)
    post.delete()
    return redirect('listar_arenas')
