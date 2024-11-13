from django.shortcuts import render,redirect, get_object_or_404
from .models import Laboratorio
from .forms import LaboratorioForm

# Create your views here.

def lista_laboratorio(request):
    visitas = request.session.get('visitas', 0)
    request.session['visitas'] = visitas + 1
    labs = Laboratorio.objects.all()
    return render(request,'laboratorio/lista.html',{'labs':labs, 'visitas':visitas })

def agregar(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')   
    else:
        form = LaboratorioForm()
    return render(request,'laboratorio/crear.html',{'form':form}) 

def actualizar(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk = pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('lista')  
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request,'laboratorio/crear.html',{'form':form})        


def eliminar(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('lista')
    return render(request,'laboratorio/eliminar.html',{'laboratorio':laboratorio})
                   