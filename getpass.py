#!/usr/bin/python

import getpass

def auth_func():
        #username = raw_input("Digite o seu login: ")
        passwd = getpass.getpass("Digite sua senha: ")

auth_func()