"""
programa feito por Marcos Henrique

chatbot luana
ediçoes feitas por ultimo:
antes dessas datas foram feitas mais coisas mas não foram registradas
6/1/18 Marcos henrique aprimorando funcs : edição do sayandprint e abrirprograma adicionado filtro de palavroes e
adicionado pesquisas na web
19/1/18 Marcos henrique ampliando os inputs de aprendizado , tem algumas coisas a serem melhoradas, e consertadas tambem
21/01/18 Marcos henrique começo da implementação de pesquisa na wikipedia, tem bastante coisa pra fazer ainda...
"""

import random
from  chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from testedois import funcs
import pyttsx3


listaprogramasexc = ['google', 'notepad', 'pycharm', 'paint']

bot =ChatBot('luana')
speaker = pyttsx3.init()
bot.set_trainer(ListTrainer)
"""
for _file in os.listdir('chats'):
    linhas = open('chats/' + _file, 'r').readlines()
    bot.train(linhas)
"""
arq = open('constart.txt', 'r')
linhas = arq.readlines()
bot.train(linhas)
while True:
    arq = open('constart.txt', 'r')
    quest = input('você: ')

    if quest == 'adicione':
       aest1 = False
       while aest1 == False:
            listai = arq.readlines()
            funcs.speak('diga a pergunta')
            v = input('bot: diga a pergunta: ')
            listatt = []
            for index, item in enumerate(listai):
                listatt.append(item.strip('\n'))
            if v in listatt:
                funcs.sayandprint('bot: ja existe no arquivo')

                aest1 = False
            else:
                listai.append('{}\n'.format(v))
                aest1 = True
                #arq = open('constart.txt', 'w')
                #arq.writelines(listai)
                #arq.close()
       aest2 = False
       while aest2 == False:

           funcs.speak('diga a resposta')
           v = input('bot: diga a resposta: ')
           listats = []
           for index, item in enumerate(listai):
               listats.append(item.strip('\n'))
           if v in listats:
               funcs.sayandprint('bot: ja existe no arquivo')
               aest2 = False
           else:
               listai.append('{}\n'.format(v))
               aest2 = True
       if aest1 == True and aest2 == True:
           arq = open('constart.txt', 'w')
           arq.writelines(listai)
           arq.close()
           arq = open('constart.txt', 'r')
           linhas = arq.readlines()
           funcs.speak('vou treinar oq eu aprendi')
           print('bot: vou treinar oq eu aprendi....')
           bot.train(linhas)
           funcs.speak('treinei')
           print('bot: treinei!')
       else:
           print('que estranho')

    elif 'abrir' in quest or quest in listaprogramasexc:
        funcs.abrirprograma(quest)
    elif 'fazer pesquisa de ' in quest:
        funcs.fazerpesquisa(quest)
    elif 'buscar definiçao de 'in quest:
        funcs.sayandprint('ainda esta em desenvolvimento...')
    else:
        frasesproibidas = ['vai tomar no cu', 'vai se fuder', 'teu cu']
        response = bot.get_response(quest)
        arq = open('constart.txt', 'r')
        linhas = arq.readlines()
        linhast = []
        for index, linhas in enumerate(linhas):
            linhast.append(linhas.strip('\n'))
        if quest in linhast:
            funcs.speak(response)
            print('bot :', response)

        elif response in frasesproibidas:
            print('bolhufas')

        else:
            an = random.choice([1,2])
            if an == 1:
                item1 = quest
                item2 = input('oque eu devo responder quando alguem me perguntar isso ?')
                funcs.speak('oque eu devo responder quando alguem me perguntar isso ?')

                arq = open('constart.txt', 'r')
                lista = arq.readlines()
                listatt = []
                for index, item in enumerate(lista):
                    listatt.append(item.strip('\n'))
                lista.append('{}\n{}\n'.format(item1, item2))
                arq = open('constart.txt', 'w')
                arq.writelines(lista)
                arq.close()
                funcs.speak('vou treinar oq eu aprendi')
                print('bot: vou treinar oq eu aprendi....')
                arq = open('constart.txt', 'r')
                linhas = arq.readlines()
                bot.train(linhas)
                funcs.speak('treinei')
                print('bot: treinei!')
            else:
                funcs.speak(response)
                print('bot :', response)

