from __future__ import absolute_import, division, print_function
import MySQLdb as mdb
def conn_sql():
	try:
		host = str(input("Digite o hostname ou ip da base: "))
		user = str(input("Digite o usuáio de acesso: "))
		passwd = str(input())
	    db = mdb.connect('localhost','datalogin','P@ssw0rd','Switchs')
	    cursor = db.cursor()
	    cursor.execute(command)
	except Exception as e:
		print("Error: %s" %e)
		db.rollback()
	finally:
	    db.commit()
	    db.close()