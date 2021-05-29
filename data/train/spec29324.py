import numpy as np 

def function(x):

	h1 = 6
	z1 = 7
	paths = []
	try:
		if z1 < 3:
			h1 = h1+8
			x = x*x
			paths.append(1)
		else:
			z1 = z1*h1
			z1 = 7+z1
			paths.append(2)
		if x > 0:
			h1 = h1-x
			z1 = 8+z1
			x = 6*x
			paths.append(3)
		else:
			x = 5*x
			h1 = 4-h1
			h1 = 9+z1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))