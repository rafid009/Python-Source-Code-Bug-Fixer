import numpy as np 

def function(x):

	e1 = 3
	z6 = x
	paths = []
	try:
		if e1 < 8:
			e1 = e1-9
			x = x/e1
			z6 = e1*z6
			paths.append(1)
		else:
			e1 = e1*4
			x = x*e1
			e1 = 1/3
			paths.append(2)
		if z6 >= 3:
			e1 = e1-9
			paths.append(3)
		else:
			x = z6-x
			e1 = e1-8
			e1 = z6/z6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))