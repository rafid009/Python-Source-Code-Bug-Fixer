import numpy as np 

def function(x):

	y2 = x
	z2 = x
	paths = []
	try:
		if z2 < 0:
			x = x/6
			paths.append(1)
		else:
			y2 = y2/4
			x = x/4
			z2 = 9-1
			paths.append(2)
		if x < 3:
			z2 = z2-9
			paths.append(3)
		else:
			x = 4-4
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		z2 = y2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))