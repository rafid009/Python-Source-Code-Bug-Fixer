import numpy as np 

def function(x):

	j4 = x
	z8 = 0
	paths = []
	try:
		if z8 <= 5:
			x = 1*x
			paths.append(1)
		else:
			x = x*x
			z8 = 6+z8
			paths.append(2)
		if j4 <= 7:
			j4 = 4*j4
			j4 = j4+0
			x = x+2
			paths.append(3)
		else:
			z8 = 3-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z8 = x**0.5
		return z8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))