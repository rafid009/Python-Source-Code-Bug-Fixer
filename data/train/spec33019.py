import numpy as np 

def function(x):

	z4 = x
	i2 = x
	x = x
	paths = []
	try:
		if z4 >= 6:
			x = 3/x
			paths.append(1)
		else:
			x = x*9
			z4 = x-7
			x = z4+0
			paths.append(2)
		if i2 >= 0:
			z4 = z4*4
			paths.append(3)
		else:
			i2 = 2/3
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))