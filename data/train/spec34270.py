import numpy as np 

def function(x):

	a6 = x
	z3 = x
	paths = []
	try:
		if x < 4:
			a6 = a6+a6
			paths.append(1)
		else:
			z3 = 0/x
			paths.append(2)
		if a6 > 9:
			a6 = z3/a6
			a6 = a6*8
			paths.append(3)
		else:
			z3 = z3/7
			z3 = x*0
			z3 = z3/a6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))