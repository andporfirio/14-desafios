#!/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import os

#Modulo para importacao do arquivo csv 

def import_csv():

	file = input('Digite o nome do arquivo .csv: ')
	list_files = []
	try:
		if '.csv' in file:
			with open(file,'rb') as csvfile:
				csvreader = csv.reader(csvfile,delimiter=' ', quotechar='|')
				for line in csvreader:
					list_files.append(','.join(line))
		else:
			print('Arquivo nao confere como um aquivo csv')
	except Exception as e:
		print(e)
	return list_files