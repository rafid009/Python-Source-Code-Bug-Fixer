import numpy as np 

def function(x):

	v2 = 7
	z3 = 9
	paths = []
	try:
		if x <= 8:
			z3 = 7*v2
			paths.append(1)
		else:
			z3 = x/8
			v2 = v2*5
			paths.append(2)
		if x > 6:
			v2 = v2-z3
			x = z3/2
			z3 = z3*8
			paths.append(3)
		else:
			v2 = x-2
			v2 = v2*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))