#!/bin/python
import string
import random

# Modulo para a geracao do hash da senha
def pass_generator(size=14,chars=string.ascii_uppercase + string.digits):
	return ''.join(random.SystemRandom().choice(chars) for _ in range(size))

