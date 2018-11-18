from __future__ import absolute_import, division, print_function
import smtplib

def sending_email(mail,uid,userpassword):
	gmail_user = 'user.desafio01@gmail.com'  
	gmail_password = 'U$3Rdesafio01'

	sent_from = gmail_user  
	to = mail  
	subject = 'User Account'  
	body = "Here your user from OpenLdap\n\n \
	        user_account = {}\n\t\tuser_password = {}".format(uid,userpassword)
	email_text = """
	 From: {}\n \
	 To: {}\n \
	 Subject: {}\n\
	 {}""".format(sent_from, to, subject, body)

	try:  
	    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    server.ehlo()
	    server.login(gmail_user, gmail_password)
	    server.sendmail(sent_from, to, email_text)
	    server.close()

	    print('Email sent!')
	except:  
	    print('Something went wrong...')