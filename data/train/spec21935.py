import numpy as np 

def function(x):

	j4 = x
	z3 = 0
	paths = []
	try:
		if z3 >= 2:
			x = x-x
			paths.append(1)
		else:
			j4 = z3*7
			paths.append(2)
		if z3 < 6:
			x = j4-6
			z3 = x*x
			z3 = x/8
			paths.append(3)
		else:
			z3 = 8+x
			x = 3/z3
			x = j4*j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))