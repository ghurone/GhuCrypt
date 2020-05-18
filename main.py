from os import system, name

import colorama
import pyperclip
import readline  # importei para conseguir editar os inputs
from colorama import Fore, Style

from crypt import criptao
from decrypt import decriptao

colorama.init()


def clear_scr():
    return system('cls' if name == 'nt' else 'clear')


def ghusoft():
    print(Fore.LIGHTRED_EX + 'G', end='')
    print(Fore.LIGHTYELLOW_EX + 'h', end='')
    print(Fore.LIGHTGREEN_EX + 'u', end='')
    print(Fore.LIGHTWHITE_EX + 'S', end='')
    print(Fore.LIGHTCYAN_EX + 'o', end='')
    print(Fore.LIGHTBLUE_EX + 'f', end='')
    print(Fore.LIGHTMAGENTA_EX + 't' + Fore.RESET)


def title():
    print(Fore.WHITE + Style.BRIGHT)
    print('''  ______   __                   ______                                   __     
 /      \ /  |                 /      \                                 /  |    
/$$$$$$  |$$ |____   __    __ /$$$$$$  |  ______   __    __   ______   _$$ |_   
$$ | _$$/ $$      \ /  |  /  |$$ |  $$/  /      \ /  |  /  | /      \ / $$   |  
$$ |/    |$$$$$$$  |$$ |  $$ |$$ |      /$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$/   
$$ |$$$$ |$$ |  $$ |$$ |  $$ |$$ |   __ $$ |  $$/ $$ |  $$ |$$ |  $$ |  $$ | __ 
$$ \__$$ |$$ |  $$ |$$ \__$$ |$$ \__/  |$$ |      $$ \__$$ |$$ |__$$ |  $$ |/  |
$$    $$/ $$ |  $$ |$$    $$/ $$    $$/ $$ |      $$    $$ |$$    $$/   $$  $$/ 
 $$$$$$/  $$/   $$/  $$$$$$/   $$$$$$/  $$/        $$$$$$$ |$$$$$$$/     $$$$/  
                                                  /  \__$$ |$$ |                
                                                  $$    $$/ $$ |                
                                                   $$$$$$/  $$/                 ''')
    print('Created by ', end='')
    ghusoft()
    print()


while True:
    clear_scr()
    title()

    print(Fore.LIGHTYELLOW_EX + 'O que deseja?' + Fore.RESET)
    print('     [1] -  Encriptar um texto')
    print('     [2] -  Desencriptar um texto')
    print('     [3] -  Sair')

    esc = input('Escolha > ')

    if esc == '1':
        clear_scr()
        title()

        print(Fore.LIGHTYELLOW_EX + 'Digite seu texto' + Fore.RESET)
        text = input('> ')
        text_crypted = criptao(text)

        print('\n' + Fore.LIGHTYELLOW_EX + 'Texto encriptado' + Fore.RESET)
        print('> ' + text_crypted)

        pyperclip.copy(text_crypted)
        print(Fore.LIGHTGREEN_EX + 'Texto copiado para o seu clipboard!' + Fore.RESET)

        input(Fore.LIGHTRED_EX + '\nPrecione ENTER para voltar ao menu...' + Fore.RESET)
    elif esc == '2':
        clear_scr()
        title()

        print(Fore.LIGHTYELLOW_EX + 'Digite o texto' + Fore.RESET)
        text = input('> ')
        text_decrypted = decriptao(text)

        print('\n' + Fore.LIGHTYELLOW_EX + 'Texto desencriptado' + Fore.RESET)
        print('> ' + text_decrypted)

        pyperclip.copy(text_decrypted)
        print(Fore.LIGHTGREEN_EX + 'Texto copiado para o seu clipboard!' + Fore.RESET)

        input(Fore.LIGHTRED_EX + '\nPrecione ENTER para voltar ao menu...' + Fore.RESET)
    elif esc == '3':
        clear_scr()
        exit(0)
