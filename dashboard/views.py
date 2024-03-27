from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DeckForm, EventoForm
from django.http import HttpResponse
from .models import Evento
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date


# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def calendar(request):

        
    return render(request, 'calendar.html')

def form_calendar(request):
    if request.method == 'POST':
        dia_selecionado = request.POST.get('diaSelecionado')
        mes_selecionado = request.POST.get('mesSelecionado')
        ano_selecionado = request.POST.get('anoSelecionado')
        data = date(ano_selecionado, mes_selecionado, dia_selecionado)

    return render(request, 'calendar.html', {'data':data})



def home(request):
    return render(request,'home.html')

def flashcards(request):
    if request.method == 'POST':
        deck_form = DeckForm(request.POST)  # Inicialize o formulário com os dados submetidos
        if deck_form.is_valid():  # Verifique se o formulário é válido
            Evento.usuario = request.user
            deck_form.save()  # Salve os dados do formulário no banco de dados
            return HttpResponse("Deck salvo com sucesso!") 
    else:
        deck_form = DeckForm()  # Caso contrário, crie um formulário em branco para ser exibido
    return render(request, 'flashcards.html', {'deck_form': deck_form})  # Renderize o template com o formulário