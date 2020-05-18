
def criptao(string):  # Função que recebe uma string pra ser encriptada
    base_list = 'ZEQUINHAzequinha'  # String que representa uma "Tabela" com os caracteres "enctiptadores"
    str_bin = ''  # String que recebe os valores, em binário, de cada caractere do texto
    string_list = []  # Lista que recebe os valores em decimal de cada binário 4b
    str_crypted = ''  # String com o texto encriptado

    for i in range(0, len(string)):
        dec = ord(string[i])  # Recebe o valor do caractere em decimal
        str_bin += f'{dec:08b}'  # Transforma esse decimal em um binário de 8b e os concatena

    # Divide os binários concatenados em 4b, e adiciona esse valor em decimal numa lista
    for i in range(0, len(str_bin), 4):
        string_list.append(int(str_bin[i:i + 4], 2))

    # Os valores em decimais são usados como índices da "Tabela", então cada valor representa um elemento
    for i, v in enumerate(string_list):
        str_crypted += base_list[v]

    return str_crypted
