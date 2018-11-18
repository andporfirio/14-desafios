#!/bin/python
# -*- coding: utf-8 -*-

import signal
from import_csv import import_csv
from pass_id import pass_generator

def rodar_programa():

	signal.signal(signal.SIGPIPE, signal.SIG_DFL) #IOError: Broken pine
	signal.signal(signal.SIGINT, signal.SIG_DFL) #KeyboardInterrupt: Ctrl+C

	users = []
	
	list_csv = import_csv()
	for line in list_csv:
		ldap_users = {
			'nome':'',
			'sobrenome':'',
			'email':'',
			'password':''
			}
		password = pass_generator()
		a = line.split(';')
		conta = a[0].lower() + '.' + a[1].lower()
		a.append(password)
		a.append(conta)
		ldap_users.update(nome = a[0])
		ldap_users.update(sobrenome = a[1])
		ldap_users.update(email = a[2])
		ldap_users.update(password = a[3])
		ldap_users.update(conta = a[-1])

		users.append(ldap_users)

	print(users)


	# 	for line in a:
	# 		ldap_users.update(nome = line[0])
	# 		ldap_users.update(sobrenome = line[1])
	# 		ldap_users.update(email = line[2])
	# 		ldap_users.update(password = line[-1])
	# 		users.append(ldap_users)
	# print(user)


		


rodar_programa()