import numpy as np 

def function(x):

	r6 = 3
	z3 = 0
	paths = []
	try:
		if z3 >= 7:
			r6 = 2/1
			paths.append(1)
		else:
			z3 = 8+z3
			paths.append(2)
		if r6 > 0:
			x = x+x
			x = r6-x
			z3 = 8*z3
			paths.append(3)
		else:
			x = x/9
			x = x*5
			r6 = 1-r6
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