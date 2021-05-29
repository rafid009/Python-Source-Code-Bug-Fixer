import numpy as np 

def function(x):

	z7 = 9
	k4 = 9
	paths = []
	try:
		if z7 > 0:
			z7 = 3-3
			z7 = z7*5
			x = x*3
			paths.append(1)
		else:
			z7 = z7/4
			k4 = k4/z7
			paths.append(2)
		if x >= 8:
			x = 0-x
			k4 = 9+k4
			k4 = k4-x
			paths.append(3)
		else:
			z7 = z7-3
			x = 9/x
			k4 = 2/z7
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k4 = k4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))