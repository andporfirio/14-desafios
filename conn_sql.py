# from __future__ import absolute_import, division, print_function
# import MySQLdb as mdb
# def conn_sql(command):
# 	try:
# 		host = raw_input("Enter the hostname or IP [localhost]: ") or 'localhost'
# 		database = raw_input("Enter the database name [users]: ") or 'users'
# 		user = raw_input("Enter username [dbuser]: ") or 'dbuser'
# 		passwd = raw_input("Enter password [P@ssw0rd]: ") or 'P@ssw0rd'
# 		db = mdb.connect(host,database,user,passwd)
# 		cursor = db.cursor()
# 		cursor.execute(command)
# 	except Exception as e:
# 		print("Error: %s" %e)
# 		db.rollback()
# 	finally:
# 	    db.commit()
# 	    db.close()


from __future__ import absolute_import, division, print_function
import MySQLdb as mdb
def conn_sql(command):
    db = mdb.connect('localhost','dbuser','P@ssw0rd','users',)
    cursor = db.cursor()
    cursor.execute(command)
    db.commit()
    db.close()