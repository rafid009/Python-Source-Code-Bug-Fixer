import numpy as np 

def function(x):

	z9 = 2
	a2 = x
	paths = []
	try:
		if z9 <= 2:
			x = 4/x
			x = 5*7
			paths.append(1)
		else:
			a2 = a2/5
			a2 = 2-a2
			paths.append(2)
		if x <= 2:
			x = 0-z9
			a2 = a2-0
			x = x/x
			paths.append(3)
		else:
			z9 = 5/4
			z9 = z9+4
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))