import numpy as np 

def function(x):

	a1 = x
	z7 = 4
	paths = []
	try:
		if a1 < 0:
			a1 = a1-1
			a1 = a1+8
			x = x*2
			paths.append(1)
		else:
			z7 = 3*z7
			a1 = a1+z7
			x = 0/x
			paths.append(2)
		if x <= 0:
			a1 = 9/a1
			paths.append(3)
		else:
			a1 = a1+6
			x = 9+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))