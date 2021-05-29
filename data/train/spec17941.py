import numpy as np 

def function(x):

	f8 = x
	z3 = 2
	paths = []
	try:
		if z3 > 6:
			f8 = 1+f8
			x = 6-x
			f8 = f8-2
			paths.append(1)
		else:
			z3 = 0+5
			f8 = f8/9
			x = 6-x
			paths.append(2)
		if z3 >= 7:
			x = x*7
			paths.append(3)
		else:
			f8 = f8-z3
			f8 = f8-0
			f8 = 3-f8
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