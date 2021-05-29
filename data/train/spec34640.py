import numpy as np 

def function(x):

	j1 = 9
	z1 = x
	paths = []
	try:
		if z1 > 5:
			z1 = j1*2
			paths.append(1)
		else:
			j1 = 3-j1
			j1 = x/j1
			paths.append(2)
		if z1 > 7:
			j1 = z1-j1
			paths.append(3)
		else:
			x = 4/x
			z1 = z1+z1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))