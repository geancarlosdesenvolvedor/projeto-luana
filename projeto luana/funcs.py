import os
import pyttsx3
import wikipedia
speaker = pyttsx3.init()
wikipedia.set_lang('pt')
def speak(text):
    speaker.say(text)
    speaker.runAndWait()
def sayandprint(text):
    v = text
    if 'bot: ' in text:
        text.replace('bot: ', '')
        speak(text)
        print(v)
    else:
        speak(text)
        print(v)
def fazerpesquisa(quest):
    questr = quest.replace('fazer pesquisa de ', '')
    questf = questr.split()
    sayandprint('bot: fazendo pesquisa de {} no google' . format(str(questf).strip('[]').replace(',', '').replace("'", '')))
    os.startfile('https://www.google.ie/search?rlz=1C1PRFI_enBR731BR731&ei=p2xRWt2WK4OcgAaOoqPgCA&q={}&oq=te&gs_l=psy-ab.3.1.35i39k1l2j0i67k1l2j0l3j0i67k1j0l2.560718.561789.0.564714.3.3.0.0.0.0.90.179.2.3.0....0...1c.1.64.psy-ab..0.3.314.6...135.qude2Vel5yM'. format(str(questf).strip('[]').replace(',', '').replace("'", '')))
"""
#ainda em desevolvimento!

def buscardefinicao(quest):

    questr = quest.replace('buscar definiçao de ', '')
    resposta = wikipedia.summary(questr, sentences=2)
    print(resposta)
"""
def abrirprograma(quest):
        questr = ''
        if 'abrir ' in quest:
            questr = quest.replace('abrir ', '')
        else:
            questr = quest

        if questr == 'google':
            sayandprint('bot: abrindo google')
            os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        elif questr == 'notepad':
            sayandprint('bot: abrindo notepad')
            os.startfile("notepad.exe")
        elif questr == 'ferramenta de captura':
            sayandprint('bot: abrindo ferramenta de captura')
            os.startfile('SnippingTool.exe')
        elif questr == 'paint':
            sayandprint('bot: abrindo paint')
            os.startfile('mspaint.exe')
        elif questr == '':
            sayandprint('bot: qual programa')
        else:
            sayandprint('bot: não encontro esse programa')
            


