class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def data_formatada(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite=1000):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def depositar(self, valor=0):
        self.__saldo += valor

    def __pode_sacar(self, saque):
        saque_maximo = self.__saldo + self.__limite
        return saque <= saque_maximo

    def sacar(self, valor=0):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('\033[0:31mO saque solicitado não é possível, pois limite foi ultrapassado.\033[m')

    def transferir(self, destino, valor=0):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigos_bancos():
        codigos = "{'BB': '001', 'Caixa': '104', 'Bradesco': '237'}".replace("'", "").replace("{", "").replace("}", "")
        return codigos


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def __str__(self):
        return f'Nome: {self._nome} Likes: {self._likes}'

    def __repr__(self):
        return f'Programa(nome={self._nome}, ano={self.ano})'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

    def __repr__(self):
        return f'Filme(nome={self._nome}, ano={self.ano}, duração={self.duracao})'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

    def __repr__(self):
        return f'Serie(nome={self._nome}, ano={self.ano}, temporadas={self.temporadas})'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)
