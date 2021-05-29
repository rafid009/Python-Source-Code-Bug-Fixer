import numpy as np 

def function(x):

	z3 = x
	f3 = x
	paths = []
	try:
		if x >= 9:
			f3 = 7/3
			paths.append(1)
		else:
			f3 = f3+1
			f3 = f3*f3
			paths.append(2)
		if x > 1:
			z3 = z3+7
			f3 = f3*7
			paths.append(3)
		else:
			f3 = f3+7
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