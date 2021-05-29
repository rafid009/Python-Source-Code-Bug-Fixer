import numpy as np 

def function(x):

	z3 = x
	j7 = 5
	paths = []
	try:
		if j7 >= 0:
			z3 = x-z3
			x = 6/x
			paths.append(1)
		else:
			j7 = 5-j7
			paths.append(2)
		if j7 > 2:
			x = 8/x
			paths.append(3)
		else:
			j7 = 9-j7
			z3 = z3-z3
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