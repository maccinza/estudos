# -*- coding: utf-8 -*-
__author__ = 'infante'


def problema_um():
    u"""
        Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
        between 2000 and 3200 (both included).
        The numbers obtained should be printed in a comma-separated sequence on a single line.
    """

    print ', '.join([str(i) for i in xrange(2000, 3201) if not i % 7 and i % 5])


def problema_dois(numero):
    u"""
        Write a program which can compute the factorial of a given numbers.
        The results should be printed in a comma-separated sequence on a single line.
        Suppose the following input is supplied to the program:
            8
        Then, the output should be:
            40320
    """
    if numero == 0:
        return 1
    else:
        return numero * problema_dois(numero-1)


def problema_tres(numero):
    u"""
        With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
        such that is an integral number between 1 and n (both included) and then the program should print the
        dictionary.
        Suppose the following input is supplied to the program:
            8
        Then, the output should be:
            {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    """

    print {i: i * i for i in xrange(1, numero + 1)}


def problema_quatro():
    u"""
        Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a
        tuple which contains every number.
        Suppose the following input is supplied to the program:
            34,67,55,33,12,98
        Then, the output should be:
            ['34', '67', '55', '33', '12', '98']
            ('34', '67', '55', '33', '12', '98')
    """

    numbers = raw_input(u"Informe uma sequência de números separados por vírgula: ")
    numbers = numbers.replace(" ", "")
    print numbers.split(",")
    print tuple(numbers.split(","))


def problema_cinco():
    u"""
        Define a class which has at least two methods:
            getString: to get a string from console input
            printString: to print the string in upper case.
    """

    class StringController(object):
        def __init__(self):
            self.text = ''

        def get_string(self):
            self.text = raw_input(u"Informe um texto para armazená-lo: ")

        def print_string(self):
            print self.text.upper()

    obj = StringController()
    obj.get_string()
    obj.print_string()