# -*- coding: utf-8 -*-
__author__ = 'infante'


def problema_seis():
    u"""
        Write a program that calculates and prints the value according to the given formula:
            Q = Square root of [(2 * C * D)/H]
        Following are the fixed values of C and H:
            C is 50. H is 30.
            D is the variable whose values should be input to your program in a comma-separated sequence.
        Example
        Let us assume the following comma separated input sequence is given to the program:
            100,150,180
        The output of the program should be:
            18,22,24
    """

    from math import sqrt
    c = 50
    h = 30

    params = raw_input(u"Informe os valores separados por vírgula: ")
    params = [int(i) for i in params.replace(" ", "").split(",")]
    print ','.join([str(int(sqrt((2 * c * d)/h))) for d in params])


def problema_sete():
    u"""
        Question:
            Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
            The element value in the i-th row and j-th column of the array should be i*j.
            Note: i=0,1.., X-1; j=0,1,..Y-1.
            Example
            Suppose the following inputs are given to the program:
            3,5
            Then, the output of the program should be:
            [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    """

    numeros = raw_input(u"Informe os as dimensões do array, dois números separados por vírgula: ")
    numeros = [int(i) for i in numeros.split(",")]
    print [[i*j for j in range(numeros[1])] for i in range(numeros[0])]


def problema_oito():
    u"""
        Question:
            Write a program that accepts a comma separated sequence of words as input and prints the words in
            a comma-separated sequence after sorting them alphabetically.
            Suppose the following input is supplied to the program:
                without,hello,bag,world
            Then, the output should be:
                bag,hello,without,world
    """

    palavras = raw_input(u"Informe as palavras separadas por vírgula: ")
    print ','.join(sorted(palavras.split(",")))


def problema_nove():
    u"""
        Question:
            Write a program that accepts sequence of lines as input and prints the lines after making all characters
            in the sentence capitalized.
            Suppose the following input is supplied to the program:
                Hello world
                Practice makes perfect
            Then, the output should be:
                HELLO WORLD
                PRACTICE MAKES PERFECT
    """

    text = []
    while True:
        s = raw_input(u"Informe o texto desta linha: ")
        if s:
            text.append(s.upper())
        else:
            break
    for t in text:
        print t


def problema_dez():
    u"""
        Question:
            Write a program that accepts a sequence of whitespace separated words as input and prints the words after
            removing all duplicate words and sorting them alphanumerically.
            Suppose the following input is supplied to the program:
                hello world and practice makes perfect and hello world again
            Then, the output should be:
                again and hello makes perfect practice world
    """

    entrada = raw_input(u"Informe as palavras separadas por espaços: ")
    palavras = [w for w in entrada.split(" ")]
    print " ".join(sorted(list(set(palavras))))


def problema_onze():
    u"""
        Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
        whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in
        a comma separated sequence.
        Example:
            0100,0011,1010,1001
        Then the output should be:
            1010
        Notes: Assume the data is input by console.
    """

    seq = raw_input(u"Informe a sequência de binários separados por vírgula: ")
    print ','.join([i for i in seq.split(",") if int(i, 2) % 5 == 0])


def problema_doze():
    u"""
        Question:
            Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each
            digit of the number is an even number.
            The numbers obtained should be printed in a comma-separated sequence on a single line.
    """
    numeros = []
    for i in xrange(1000, 3001):
        flag = True
        for caractere in str(i):
            if int(caractere) % 2 == 0:
                flag = False
                break
        if flag:
            numeros.append(str(i))
    print ",".join(numeros)


def problema_treze():
    u"""
        Write a program that accepts a sentence and calculate the number of letters and digits.
        Suppose the following input is supplied to the program:
            hello world! 123
        Then, the output should be:
            LETTERS 10
            DIGITS 3
    """
    letras = 0
    numeros = 0
    entrada = raw_input(u"Informe a sua string de entrada: ")
    for caractere in entrada:
        if caractere.isdigit():
            numeros += 1
        elif caractere.isalpha():
            letras += 1
    print "LETRAS {0}".format(letras)
    print "DIGITOS {0}".format(numeros)


def problema_quatorze():
    u"""
        Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
        Suppose the following input is supplied to the program:
        Hello world!
        Then, the output should be:
            UPPER CASE 1
            LOWER CASE 9
    """

    uppercase = 0
    lowercase = 0
    entrada = raw_input(u"Informe a sua string de entrada: ")
    for caractere in entrada:
        if caractere.isupper():
            uppercase += 1
        elif caractere.islower():
            lowercase += 1
        else:
            pass
    print "UPPER: {0}".format(uppercase)
    print "LOWER: {0}".format(lowercase)


def problema_quinze():
    u"""
        Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
        Suppose the following input is supplied to the program:
            9
        Then, the output should be:
            11106
    """

    entrada = raw_input(u"Informe um dígito de entrada: ")
    soma = sum([int(entrada * quantidade) for quantidade in range(1, 5)])
    print soma


def problema_dezesseis():
    u"""
        Use a list comprehension to square each odd number in a list. The list is input by a sequence of
        comma-separated numbers. Suppose the following input is supplied to the program:
            1,2,3,4,5,6,7,8,9
        Then, the output should be:
            1,9,25,49,81
    """

    entrada = raw_input(u"Informe uma sequéncia de números separados por vírgula: ")
    print ','.join([str(int(numero)**2) for numero in entrada.split(',') if int(numero) % 2])


def problema_dezessete():
    u"""
        Write a program that computes the net amount of a bank account based a transaction log from console input.
        The transaction log format is shown as following:
            D 100
            W 200
            ¡­
            D means deposit while W means withdrawal.
            Suppose the following input is supplied to the program:
            D 300
            D 300
            W 200
            D 100
        Then, the output should be:
            500
    """
problema_dezesseis()
