import numpy as np 

def function(x):

	i8 = x
	z0 = x
	x = 5
	paths = []
	try:
		if x < 4:
			i8 = 8+i8
			i8 = z0-2
			paths.append(1)
		else:
			i8 = i8-i8
			paths.append(2)
		if z0 > 9:
			x = x+2
			z0 = z0/3
			paths.append(3)
		else:
			i8 = 9*i8
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))