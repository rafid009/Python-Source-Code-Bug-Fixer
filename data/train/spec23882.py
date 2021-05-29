import numpy as np 

def function(x):

	z7 = 9
	e9 = x
	paths = []
	try:
		if x >= 0:
			z7 = z7*z7
			paths.append(1)
		else:
			x = e9*z7
			e9 = e9-9
			paths.append(2)
		if x <= 3:
			x = 1/x
			paths.append(3)
		else:
			e9 = z7*0
			x = z7/z7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))