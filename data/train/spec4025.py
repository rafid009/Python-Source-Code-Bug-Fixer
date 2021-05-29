import numpy as np 

def function(x):

	z3 = x
	o6 = x
	paths = []
	try:
		if o6 > 9:
			o6 = o6+x
			paths.append(1)
		else:
			z3 = 5+z3
			o6 = o6-9
			z3 = 6*z3
			paths.append(2)
		if z3 > 5:
			o6 = 1-7
			x = x*1
			z3 = o6+z3
			paths.append(3)
		else:
			o6 = o6-z3
			o6 = o6*8
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