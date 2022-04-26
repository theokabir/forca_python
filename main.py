import numpy as np
from sprites import SPRITES
import glob, os, random


def main():
    apagar()
    digitar = input("deseja digitar sua propria palavra? (s/n)").lower()
    if digitar == "s":
        palavra = input("insira a palavra para a forca (sem acentos ou simbolos):: ")
        apagar()
        forca(palavra.strip().lower())
    else:
        listas = []
        for file in glob.glob("listas/*.txt"):
            arquivo = file[:-4].split("\\")
            listas.append(arquivo[-1])
        apagar()

        print("listas: ")
        print("="*25)
        for opcao in listas:
            print(opcao)
        print("="*25)
            
        while True:
            op = input("digite a lista que quer usar:: ").strip().lower()
            if np.isin([op], listas):
                lista = open(f'listas/{op}.txt', 'r').read().splitlines()
                choice = random.choice(lista)
                apagar()
                forca(choice.strip().lower())
                break
            else:
                print("digite uma opção válida")

def forca(p):
    separacao = p.split(" ")
    word_indexes = []
    corretas = []
    falhas = []
    total_chances = len(SPRITES)
    estado = 0
    amostragem = ""
    reiniciar = True
    
    while True:
        try:
            
            amostragem = gerar_amostragem(corretas, word_indexes, separacao)
            print(SPRITES[estado])
            print(f"falhas: {falhas}")
            print(amostragem)
            
            if "_" not in amostragem or estado == total_chances-1:
                
                if "_" not in amostragem:
                    print("VOCÊ GANHOU!!!!!!!")
                    
                elif estado == total_chances-1:
                    print("VOCÊ PERDEU")
                    
                continuar = input("deseja jogar novamente? (s/n)").lower().strip()
                
                if continuar == "s":
                    apagar()
                    break
                else:
                    apagar()
                    print("muito obrigado por jogar\n[Enter] para finalizar")
                    input("")
                    reiniciar = False
                    break
                
                
            nova_letra = input("insira uma letra:: ").strip().lower()
            
            if not nova_letra == "":
            
                if nova_letra == p:
                    corretas += list(p)
                elif nova_letra in separacao:
                    word_indexes.append(separacao.index(nova_letra))  
                elif nova_letra[0] in falhas:
                    pass
                elif nova_letra[0] in p:
                    corretas.append(nova_letra[0])
                else:
                    falhas.append(nova_letra[0])
                    estado += 1
                
            apagar()
            
        except:
          print("hove algum erro no programa, pressione Enter para reiniciar")
          input("")
          main()  
    
    if reiniciar:
        main()

def apagar():
    os.system("cls") or None
    
def gerar_amostragem(corretas, word_indexes, separacao):
    amostragem = ""
    for i in range(len(separacao)):
        if i in word_indexes:
            amostragem += separacao[i]
        else:
            for letra in separacao[i]:
                if letra == " " or letra == "-":
                    amostragem += letra
                elif np.isin([letra], corretas):
                    amostragem += letra
                else:
                    amostragem += "_"
        amostragem += " "
    
    return amostragem


if __name__ == "__main__":
    main()