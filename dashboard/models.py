from django.db import models

# Create your models here.
class Deck (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
class Flashcard(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    pergunta = models.TextField()
    resposta = models.TextField()

    def __str__(self):
        return f"Flashcard: {self.pergunta}"