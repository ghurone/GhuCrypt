from os import system, name

import colorama
import pyperclip
import readline  # importei para conseguir editar os inputs
from colorama import Fore, Style

from zequinha import Zequinha

colorama.init()
chave = Zequinha()


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
    print('   ______   __                   ______                                   __     \n'
          '  /      \ /  |                 /      \                                 /  |    \n'
          ' /$$$$$$  |$$ |____   __    __ /$$$$$$  |  ______   __    __   ______   _$$ |_   \n'
          ' $$ | _$$/ $$      \ /  |  /  |$$ |  $$/  /      \ /  |  /  | /      \ / $$   |  \n'
          ' $$ |/    |$$$$$$$  |$$ |  $$ |$$ |      /$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$/   \n'
          ' $$ |$$$$ |$$ |  $$ |$$ |  $$ |$$ |   __ $$ |  $$/ $$ |  $$ |$$ |  $$ |  $$ | __ \n'
          ' $$ \__$$ |$$ |  $$ |$$ \__$$ |$$ \__/  |$$ |      $$ \__$$ |$$ |__$$ |  $$ |/  |\n'
          ' $$    $$/ $$ |  $$ |$$    $$/ $$    $$/ $$ |      $$    $$ |$$    $$/   $$  $$/ \n'
          '  $$$$$$/  $$/   $$/  $$$$$$/   $$$$$$/  $$/        $$$$$$$ |$$$$$$$/     $$$$/  \n'
          '                                                   /  \__$$ |$$ |                \n'
          '                                                   $$    $$/ $$ |                \n'
          '                                                    $$$$$$/  $$/                 ')
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
    print()

    esc = input('>>> ')

    if esc == '1':
        clear_scr()
        title()

        print(Fore.LIGHTYELLOW_EX + 'Digite seu texto' + Fore.RESET)
        text = input('> ')
        text_crypted = chave.encriptar(text)

        print('\n' + Fore.LIGHTYELLOW_EX + 'Texto encriptado' + Fore.RESET)
        print('> ' + text_crypted)

        pyperclip.copy(text_crypted)
        print()
        print(Fore.LIGHTGREEN_EX + 'Texto copiado para o seu clipboard!' + Fore.RESET)

        input(Fore.LIGHTRED_EX + '\nAperte ENTER para voltar ao menu...' + Fore.RESET)
    elif esc == '2':
        clear_scr()
        title()

        print(Fore.LIGHTYELLOW_EX + 'Digite o texto' + Fore.RESET)
        text = input('> ')
        try:
            text_decrypted = chave.desencriptar(text)

            print('\n' + Fore.LIGHTYELLOW_EX + 'Texto desencriptado' + Fore.RESET)
            print('> ' + text_decrypted)

            pyperclip.copy(text_decrypted)
            print()
            print(Fore.LIGHTGREEN_EX + 'Texto copiado para o seu clipboard!' + Fore.RESET)

            input(Fore.LIGHTRED_EX + '\nAperte ENTER para voltar ao menu...' + Fore.RESET)
        except ValueError:
            print('O texto não está escrito em Zequinhês')
            input(Fore.LIGHTRED_EX + '\nAperte ENTER para voltar ao menu...' + Fore.RESET)

    elif esc == '3':
        clear_scr()
        exit(0)
