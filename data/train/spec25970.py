import numpy as np 

def function(x):

	z3 = 2
	w5 = 7
	paths = []
	try:
		if x <= 9:
			z3 = z3/x
			w5 = z3-2
			paths.append(1)
		else:
			z3 = w5*0
			w5 = w5+0
			x = 5-0
			paths.append(2)
		if x >= 7:
			x = 9*x
			w5 = w5-2
			paths.append(3)
		else:
			z3 = w5/x
			z3 = 3-z3
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		z3 = z3**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))