from random import Random

class Zequinha:

    def __init__(self, seed = None) -> None:
        self.base = list('ZEQUINHAzequinha')  # Chave base
        
        # Caso insira uma seed ele embaralha a chave base em relação a essa seed.
        if seed != None:
            Random(seed).shuffle(self.base)

    def encriptar(self, string:str) -> str:
        if isinstance(string, str):
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
                str_crypted += self.base[v]

            return str_crypted
        
        raise TypeError("O paramêtro `string` precisa ser do tipo STR")

    def desencriptar(self, string:str) -> str:
        if self.__is_zeca(string):
            list_index = []  # Lista que contém os índices de cada caractere em relação a "Tabela"
            string_decr = ''  # String que guarda os binários dos índices concatenados
            str_decrypted = ''  # String que armazena os binários transformados em caracteres (bin -> dec - > char)

            # Acha o respectivo índice na tabela pelo valor de cada elemento da string
            for i in range(0, len(string)):
                list_index.append(self.base.index(string[i]))

            # Transforma cada índice em binário de 4b e os concatena
            for i, v in enumerate(list_index):
                string_decr += f'{v:04b}'  # Os binários são de 4b, por se tratar de uma tabela de 16 char

            # Divide a string_decr em grupos de 8b, e transforma o binário em decimal e de decimal para ascii
            for i in range(0, len(string_decr), 8):
                str_decrypted += chr(int(string_decr[i: i+8], 2))

            return str_decrypted
        
        raise ValueError('A string inserida não está em Zequinha.')

    def __is_zeca(self, string: str) -> bool:
        """
            Método que verifica se todos os caracteres da string inserida
        estão contidos na chave base.
        """
        if isinstance(string, str):
            letras = set(string)  # um set() com todos os chars da string

            for letra in letras:
                if letra not in self.base:
                    return False
            
            return True
        
        raise TypeError("O paramêtro `string` precisa ser do tipo STR")
