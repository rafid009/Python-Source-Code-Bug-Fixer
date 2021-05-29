import numpy as np 

def function(x):

	z3 = x
	b7 = 4
	paths = []
	try:
		if x < 4:
			b7 = z3+4
			paths.append(1)
		else:
			z3 = 5*z3
			paths.append(2)
		if b7 <= 8:
			z3 = 2*6
			paths.append(3)
		else:
			b7 = b7*7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))