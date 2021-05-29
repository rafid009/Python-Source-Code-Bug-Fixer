import numpy as np 

def function(x):

	z3 = 1
	l3 = x
	paths = []
	try:
		if x < 8:
			z3 = z3-l3
			paths.append(1)
		else:
			l3 = z3*4
			x = 6-0
			paths.append(2)
		if z3 > 7:
			z3 = 1+z3
			x = l3/4
			z3 = 9+1
			paths.append(3)
		else:
			z3 = z3+1
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		x = z3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))