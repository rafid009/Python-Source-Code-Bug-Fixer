import numpy as np 

def function(x):

	z2 = 0
	y5 = 5
	paths = []
	try:
		if y5 >= 8:
			y5 = z2*y5
			y5 = y5/6
			paths.append(1)
		else:
			z2 = 9+1
			y5 = y5+6
			paths.append(2)
		if x < 0:
			z2 = z2+5
			paths.append(3)
		else:
			x = 3-z2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))