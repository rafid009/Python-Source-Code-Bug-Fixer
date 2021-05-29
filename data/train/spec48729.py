import numpy as np 

def function(x):

	z3 = x
	x0 = 6
	paths = []
	try:
		if x0 <= 4:
			z3 = x*z3
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if z3 > 1:
			x0 = x0*1
			paths.append(3)
		else:
			x0 = 1*x
			x0 = x-9
			x0 = x0*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))