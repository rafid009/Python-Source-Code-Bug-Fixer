import numpy as np 

def function(x):

	z3 = x
	o8 = 7
	paths = []
	try:
		if x > 5:
			z3 = 9*z3
			z3 = o8+1
			paths.append(1)
		else:
			z3 = z3-7
			z3 = 5/z3
			z3 = o8+6
			paths.append(2)
		if o8 >= 3:
			z3 = x-8
			paths.append(3)
		else:
			x = 3+x
			x = 0+2
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z3 = x**0.5
		return z3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))