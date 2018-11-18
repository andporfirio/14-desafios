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

	print("Sending account data to mail users.\n########")

	for line in users:
		print('Sending mail to: {}'.format(line.get('mail')))
		sending_email(line.get('mail'),line.get('uid'),line.get('userpassword'))

	ask = raw_input('Do you want save the users account on a database? [Y/N]: ')
	if ask == 'Y':
		print('Save users account on database.\n########')

		for line in users:
			cols_info = line.keys()
			vals_info = line.values()
			insert_info = ("INSERT INTO UsersInfo ({}) VALUES ({})").format(', '.join(cols_info),vals_info)
			data = (insert_info.replace('[','').replace(']',''))
			conn_sql(data)
			
		print('Print ldif output.\n########')
		for line in users:
			print('dn: cn=%s,ou=people,dc=example,dc=com' %(line.get('cn')))

	elif ask == 'N':
		print('Print ldif output.\n########')
		for line in users:
			print('dn: cn=%s,ou=people,dc=example,dc=com' %(line.get('cn')))
			for k,v in line.items():
				print('%s: %s' %(k,v))
	else:
		print('Invalid Option')

rodar_programa()