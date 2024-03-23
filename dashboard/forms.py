from django import forms
from .models import Deck, Flashcard

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['nome', 'descricao']
        labels = {
            'nome': 'Nome do Deck',
            'descricao': 'Descrição do Deck',
        }

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['deck', 'pergunta', 'resposta']
        labels = {
            'deck': 'Deck',
            'pergunta': 'Pergunta',
            'resposta': 'Resposta',
        }
