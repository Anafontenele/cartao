from django.shortcuts import render
from cartaoApp.forms import ValidarForm
from cartaoApp.models import Validar

# Create your views here.
def ola(request):
    return render(request,'cartao/ola.html')

def index(request):
    return  render(request,'cartao/index.html')

def consulta(request):
    form =  ValidarForm(request.POST)
    if request.method== "POST":
        form=ValidarForm(request.POST,request.POST, request.FILES)
        if form.is_valid():
            obj= form.save()
            obj.save()
            form=ValidarForm
    return  render(request,'cartao/consulta.html',{'form': form})


def mostrar(request):
    cartoes = Validar.objects.all()
    return render(request, 'cartao/mostrar.html', {'cartoes':cartoes})