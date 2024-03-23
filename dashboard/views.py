from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import DeckForm, FlashcardForm
from django.http import HttpResponse

# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def calendar(request):
    return render(request, 'calendar.html')

def home(request):
    return render(request,'home.html')

def flashcards(request):
    if request.method == 'POST':
        deck_form = DeckForm(request.POST)  # Inicialize o formulário com os dados submetidos
        if deck_form.is_valid():  # Verifique se o formulário é válido
            deck_form.save()  # Salve os dados do formulário no banco de dados
            return HttpResponse("Deck salvo com sucesso!")  # Ou redirecione para outra página
    else:
        deck_form = DeckForm()  # Caso contrário, crie um formulário em branco para ser exibido
    return render(request, 'flashcards.html', {'deck_form': deck_form})  # Renderize o template com o formulário