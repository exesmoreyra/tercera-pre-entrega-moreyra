from django.shortcuts import render



from django.shortcuts import render, redirect
from .forms import PaisForm, ClienteForm

def crear_pais(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core/index.html')  
        form = PaisForm()
    return render(request, 'index.html', {'form': form})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core/index.html')  
    else:
        form = ClienteForm()
    return render(request, 'index.html', {'form': form})



def home(request):
    return render(request, "cliente/index.html")


from django.shortcuts import render
from .models import Cliente
from .forms import BusquedaForm

def buscar_cliente(request):
    resultados = None
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            #realizar busquerda
            resultados = Cliente.objects.filter(nombre__icontains=termino_busqueda)
    else:
        form = BusquedaForm()

    return render(request, 'cliente/buscar_cliente.html', {'form': form, 'resultados': resultados})