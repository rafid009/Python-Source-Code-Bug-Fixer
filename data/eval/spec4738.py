import numpy as np 

def function(x):

	z4 = x
	k4 = x
	x = 5
	paths = []
	try:
		if x <= 5:
			x = 1+x
			k4 = 8/k4
			k4 = k4+z4
			paths.append(1)
		else:
			x = z4*k4
			paths.append(2)
		if k4 > 1:
			x = 7+x
			paths.append(3)
		else:
			z4 = x+k4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		z4 = k4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))