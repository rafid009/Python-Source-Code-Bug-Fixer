import numpy as np 

def function(x):

	z3 = 7
	l7 = x
	paths = []
	try:
		if x >= 3:
			l7 = 9+l7
			z3 = 4+4
			paths.append(1)
		else:
			l7 = l7/3
			l7 = l7-5
			paths.append(2)
		if z3 < 5:
			x = x-l7
			l7 = x/1
			x = z3-6
			paths.append(3)
		else:
			l7 = 0*l7
			l7 = l7-7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		z3 = l7**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))