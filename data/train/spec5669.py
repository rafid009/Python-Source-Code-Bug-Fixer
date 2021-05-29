import numpy as np 

def function(x):

	z0 = x
	g5 = x
	paths = []
	try:
		if x <= 0:
			z0 = z0*7
			x = 7+x
			paths.append(1)
		else:
			x = x+g5
			paths.append(2)
		if x <= 7:
			x = x*x
			paths.append(3)
		else:
			x = g5/x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))