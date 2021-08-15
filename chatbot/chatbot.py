# Algoritmo para um chatbot bem básico

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download   # importando para corrigir um problema com o chatbot


download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


chatbot = ChatBot('Bot Abacate', tagger_language=ENGSM)

conversa = [    # uma conversa para treinar o chatbot
    'Ola',
    'Olá! Tudo bem?',
    'Tranquilo',
    'Alguma novidade?',
    'Estou programando um chatbot',
    'Nossa, maneiro',
    'Legal, né?',
    'Muito!'
]

trainer = ListTrainer(chatbot)
trainer.train(conversa)    # treino do chatbot

while True:
    mensagem = input('Mande uma mensagem para o chatbot: ')
    if mensagem == 'parar':
        break
    resposta = chatbot.get_response(mensagem)
    print(resposta)

chatbot.storage.drop()