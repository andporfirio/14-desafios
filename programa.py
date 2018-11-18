#!/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
import signal
from import_csv import import_csv
from pass_id import pass_generator
from send_mail import sending_email
from conn_sql import conn_sql

def rodar_programa():

	signal.signal(signal.SIGPIPE, signal.SIG_DFL) #IOError: Broken pine
	signal.signal(signal.SIGINT, signal.SIG_DFL) #KeyboardInterrupt: Ctrl+C

	users = []
	
	list_csv = import_csv()
	for line in list_csv:
		ldap_users = {
			'objectclass': 'inetOrgPerson',
			'cn':'',
			'sn':'',
			'mail':'',
			'userpassword':'',
			'uid':'',
			'pwdMinAge': 0
			}
		password = pass_generator()
		a = line.split(';')
		conta = line[0].lower() + a[1].lower()
		a.append(password)
		a.append(conta)
		ldap_users.update(cn = a[0] + ' ' + a[1])
		ldap_users.update(sn = a[1])
		ldap_users.update(mail = a[2])
		ldap_users.update(userpassword = a[3])
		ldap_users.update(uid = a[-1])
		users.append(ldap_users)

	# print("Sending account data to mail users.\n")

	# for line in users:
	# 	print('Sending mail to: {}'.format(line.get('mail')))
	# 	sending_email(line.get('mail'),line.get('uid'),line.get('userpassword'))

	print('Save users account on database.')

	for line in users:
		for k,v in line.items():
			cols_info = k
			vals_info = v
			insert_info = ("INSERT INTO UsersInfo (%s) VALUES ('%s')" %(k,v))
			conn_sql(insert_info)
			
		# insert_info = ("INSERT INTO UsersInfo ({}) VALUES ({})").format(cols_info,vals_info)
		# print(insert_info)
		# insert_info = ("INSERT INTO UsersInfo ({}) VALUES ('{}')"
		# 			  .format(cols_info,vals_info)
					  # .format(",".join(cols_info), "','".join(vals_info)))
		#conn_sql(insert_info)	
        # cols_info = line.keys()
        # vals_info = line.values()
        # insert_info = ("INSERT INTO UsersInfo (%s) VALUES ('%s')" %
        # 	(",".join(cols_info), "','".join(vals_info)))
        # conn_sql(insert_info)




	# for line in users:
	# 	print('dn: cn={},ou=people,dc=example,dc=com').format(line.get('cn'))
	# 	for k,v in line.items():
	# 		print('{}: {}').format(k,v)



	# 	for line in a:
	# 		ldap_users.update(nome = line[0])
	# 		ldap_users.update(sobrenome = line[1])
	# 		ldap_users.update(email = line[2])
	# 		ldap_users.update(password = line[-1])
	# 		users.append(ldap_users)
	# print(user)


		


rodar_programa()