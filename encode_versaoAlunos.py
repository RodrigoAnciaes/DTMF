
#importe as bibliotecas
from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

#funções a serem utilizadas
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)




def main():
    
    signal = signalMeu()

    #********************************************instruções*********************************************** 
    # seu objetivo aqui é gerar duas senoides. Cada uma com frequencia corresposndente à tecla pressionada
    # então inicialmente peça ao usuário para digitar uma tecla do teclado numérico DTMF
    # agora, voce tem que gerar, por alguns segundos, suficiente para a outra aplicação gravar o audio, duas senoides com as frequencias corresposndentes à tecla pressionada, segundo a tabela DTMF
    # Essas senoides tem que ter taxa de amostragem de 44100 amostras por segundo, entao voce tera que gerar uma lista de tempo correspondente a isso e entao gerar as senoides
    # Lembre-se que a senoide pode ser construída com A*sin(2*pi*f*t)
    # O tamanho da lista tempo estará associada à duração do som. A intensidade é controlada pela constante A (amplitude da senoide). Construa com amplitude 1.
    # Some as senoides. A soma será o sinal a ser emitido.
    # Utilize a funcao da biblioteca sounddevice para reproduzir o som. Entenda seus argumento.
    # Grave o som com seu celular ou qualquer outro microfone. Cuidado, algumas placas de som não gravam sons gerados por elas mesmas. (Isso evita microfonia).
    
    # construa o gráfico do sinal emitido e o gráfico da transformada de Fourier. Cuidado. Como as frequencias sao relativamente altas, voce deve plotar apenas alguns pontos (alguns periodos) para conseguirmos ver o sinal
    

    print("Inicializando encoder")
    dicFrequencies = {'1':(697,1209), '2':(697,1336), '3':(697,1477), 'A':(697,1633), '4':(770,1209), '5':(770,1336), '6':(770,1477), 'B':(770,1633), '7':(852,1209), '8':(852,1336), '9':(852,1477), 'C':(852,1633),'0':(941,1336), '#':(941,1477), 'D':(941,1633)}
    print("Aguardando usuário")
    key = input("Digite uma tecla do teclado numérico DTMF: ")
    print("Tecla digitada: ", key)
    print("Gerando Tons base")
    fs = 48000
    duration = 1
    t = np.linspace(0, duration, duration*fs, False)
    print("Gerando Tons")
    tone1 = np.sin(dicFrequencies[key][0] * 2 * np.pi * t)
    tone2 = np.sin(dicFrequencies[key][1] * 2 * np.pi * t)
    print("Somando Tons")
    tone = tone1 + tone2
    print("Executando as senoides (emitindo o som)")
    print("Gerando Tom referente ao símbolo : {}".format(key))
    #sd.play(tone, fs)
    sd.play(tone, fs, loop = True)
    sd.wait()
    # Exibe gráficos
    print("Gerando gráficos")
    plt.figure(1)
    plt.title("Sinal")
    plt.xlabel("Tempo")
    plt.ylabel("Amplitude")
    plt.plot(tone)
    plt.figure(2)
    plt.title("Transformada de Fourier")
    plt.xlabel("Frequência")
    plt.ylabel("Amplitude")
    x,y = signal.calcFFT(tone, fs)
    plt.plot(x,y)
    plt.show()
    # aguarda fim do audio
    sd.wait()
    #plotFFT(self, signal, fs)
    

if __name__ == "__main__":
    main()
