#-*- coding: utf-8 -*-
__author__ = 'infante'

import re
from math import sqrt

def problema_dezoito():
    u"""
        A website requires the users to input username and password to register.
        Write a program to check the validity of password input by users.
        Following are the criteria for checking the password:
            1. At least 1 letter between [a-z]
            2. At least 1 number between [0-9]
            1. At least 1 letter between [A-Z]
            3. At least 1 character from [$#@]
            4. Minimum length of transaction password: 6
            5. Maximum length of transaction password: 12
            Your program should accept a sequence of comma separated passwords and will check them according
            to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
            Example
                If the following passwords are given as input to the program:
                    ABd1234@1,a F1#,2w3E*,2We3345
                Then, the output of the program should be:
                    ABd1234@1
    """

    minusculas = re.compile(r'[a-z]')
    numeros = re.compile(r'[0-9]')
    maiusculas = re.compile(r'[A-Z]')
    especiais = re.compile(r'[$#@]')
    tam_min = 6
    tam_max = 12
    entrada = raw_input(u"Informe as senhas separadas por vírgulas: ")

    validos = []

    for senha in entrada.split(","):
        condicao_tamanho = tam_min <= len(senha) <= tam_max
        condicao_letras = len(minusculas.findall(senha)) >= 1 and len(maiusculas.findall(senha)) >= 1
        condicao_num_espec = len(numeros.findall(senha)) >= 1 and len(especiais.findall(senha)) >= 1
        if condicao_tamanho and condicao_letras and condicao_num_espec:
            validos.append(senha)

    print ','.join(validos)


def problema_dezenove():

    u"""
        Question:
        You are required to write a program to sort the (name, age, height) tuples by
        ascending order where name is string, age and height are numbers.
        The tuples are input by console. The sort criteria is:
            1: Sort based on name;
            2: Then sort based on age;
            3: Then sort by height.
        The priority is that name > age > score.
        If the following tuples are given as input to the program:
            Tom,19,80
            John,20,90
            Jony,17,91
            Jony,17,93
            Json,21,85
        Then, the output of the program should be:
        [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
    """

    informacoes = []
    entrada = tuple(raw_input(u"Informe nome, idade e altura do indivíduo separados por vírgulas: ").split(","))
    while entrada:
        informacoes.append(entrada)
        entrada = tuple(raw_input(u"Informe nome, idade e altura do indivíduo separados por vírgulas: ").split(","))
    print sorted(informacoes, key=lambda info_pessoal: (info_pessoal[0], info_pessoal[1], info_pessoal[2]))


def problema_vinte():
    u"""
        Question:
            A robot moves in a plane starting from the original point (0,0).
            The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
            The trace of robot movement is shown as the following:
                UP 5
                DOWN 3
                LEFT 3
                RIGHT 2
                ¡­
                The numbers after the direction are steps.
                Please write a program to compute the distance from current position after a sequence of movement and
                original point. If the distance is a float, then just print the nearest integer.
                Example:
                    If the following tuples are given as input to the program:
                        UP 5
                        DOWN 3
                        LEFT 3
                        RIGHT 2
                    Then, the output of the program should be:
                        2
    """

    coordenadas = [0, 0]
    entrada = raw_input(u"Informe uma direção (UP, DOWN, LEFT, RIGHT) e um valor inteiro, separados por espaço: ")
    while entrada:
        comando, distancia = entrada.split(' ')
        if comando == 'UP':
            coordenadas[1] += int(distancia)
        elif comando == 'DOWN':
            coordenadas[1] -= int(distancia)
        elif comando == 'RIGHT':
            coordenadas[0] += int(distancia)
        elif comando == 'LEFT':
            coordenadas[0] -= int(distancia)
        entrada = raw_input(u"Informe uma direção (UP, DOWN, LEFT, RIGHT) e um valor inteiro, separados por espaço: ")

    print int(sqrt(coordenadas[0]**2 + coordenadas[1]**2))

problema_vinte()
