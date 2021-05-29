import numpy as np 

def function(x):

	v1 = x
	z4 = 6
	paths = []
	try:
		if x > 6:
			v1 = v1/2
			v1 = v1/2
			paths.append(1)
		else:
			z4 = z4-6
			z4 = 2+7
			paths.append(2)
		if z4 < 5:
			v1 = v1/4
			x = x*x
			v1 = 3/v1
			paths.append(3)
		else:
			z4 = v1+4
			v1 = 0-3
			z4 = 8-z4
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))