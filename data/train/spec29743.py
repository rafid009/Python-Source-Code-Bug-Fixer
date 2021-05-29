import numpy as np 

def function(x):

	z3 = x
	d6 = 1
	paths = []
	try:
		if d6 >= 6:
			d6 = 3-7
			d6 = 7-d6
			paths.append(1)
		else:
			d6 = 2/1
			x = 2*x
			z3 = z3+9
			paths.append(2)
		if x > 6:
			x = 9+x
			paths.append(3)
		else:
			d6 = 3*d6
			d6 = z3*z3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))