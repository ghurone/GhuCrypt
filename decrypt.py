
def decriptao(string):  # função que recebe uma string encriptada
    base_list = 'ZEQUINHAzequinha'  # String que representa uma "Tabela"
    list_index = []  # Lista que contém os índices de cada caractere em relação a "Tabela"
    string_decr = ''  # String que guarda os binários dos índices concatenados
    str_decrypted = ''  # String que armazena os binários transformados em caracteres (bin -> dec - > char)

    # Acha o respectivo índice na tabela pelo valor de cada elemento da string
    for i in range(0, len(string)):
        list_index.append(base_list.index(string[i]))

    # Transforma cada índice em binário de 4b e os concatena
    for i, v in enumerate(list_index):
        string_decr += f'{v:04b}'  # Os binários são de 4b, por se tratar de uma tabela de 16 char

    # Divide a string_decr em grupos de 8b, e transforma o binário em decimal e de decimal para ascii
    for i in range(0, len(string_decr), 8):
        str_decrypted += chr(int(string_decr[i: i+8], 2))

    return str_decrypted
