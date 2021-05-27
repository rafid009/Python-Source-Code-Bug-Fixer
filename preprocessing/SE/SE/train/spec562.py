import numpy as np 

def function(x):

	e0 = x
	z7 = x
	x = x
	paths = []
	try:
		if x <= 9:
			x = z7-x
			x = 2*5
			paths.append(1)
		else:
			x = x-7
			z7 = 1*z7
			paths.append(2)
		if z7 <= 5:
			x = x*6
			e0 = e0+e0
			x = x-z7
			paths.append(3)
		else:
			x = x-3
			e0 = x/e0
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		z7 = z7**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))