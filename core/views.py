from django.shortcuts import render, redirect, get_object_or_404
from .models import ResetaP
from .forms import DatosForm
from .forms import ResetaPForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

def Iniciar(request):
    return render(request,'core/Iniciar.html')

def Datos(request):
    data = {
        'form': DatosForm()
    }

    if request.method == 'POST':
        formulario = DatosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Datos Guardados"
            return redirect(to='Carrito')
        else:
            data["form"] = formulario

    return render(request,'core/Datos.html', data)

def Carrito(request): 

    data = {
        'form': ResetaPForm()
    }

    if request.method == 'POST':
        formulario = ResetaPForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Reseta Guardada Exitosamente!")
            return redirect(to='Reseta')
        else:
            data["form"] = formulario

    return render(request,'core/Carrito.html', data)
    
def Reseta(request):
    resetaps = ResetaP.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(resetaps, 5)
        resetaps = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': resetaps,
        'paginator': paginator
    }

    return render(request,'core/Reseta.html', data)



def editar_medic(request, id):

    resetap = get_object_or_404(ResetaP, id=id)

    data = {
        'form': ResetaPForm(instance=resetap)
    }

    if request.method == 'POST':
        formulario = ResetaPForm(data=request.POST, instance=resetap, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "¡Modificacion Exitosa!")
            return redirect(to='Reseta')
        data["form"] = formulario

    return render(request, 'core/editar.html', data)

def eliminar_medic(request, id):
    resetap = get_object_or_404(ResetaP, id=id)
    resetap.delete()
    messages.success(request, "¡Eliminado Correctamente!")
    return redirect(to='Reseta')

