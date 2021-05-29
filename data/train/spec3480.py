import numpy as np 

def function(x):

	z3 = x
	v7 = 4
	paths = []
	try:
		if v7 >= 6:
			v7 = v7-1
			v7 = v7/z3
			paths.append(1)
		else:
			x = x+7
			x = x-9
			v7 = 8-v7
			paths.append(2)
		if v7 < 7:
			z3 = z3/5
			paths.append(3)
		else:
			z3 = z3-v7
			v7 = v7*5
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