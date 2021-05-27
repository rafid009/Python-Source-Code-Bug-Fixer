import numpy as np 

def function(x):

	z5 = x
	u6 = 0
	paths = []
	try:
		if x >= 4:
			z5 = 4+6
			z5 = x/z5
			x = x/x
			paths.append(1)
		else:
			z5 = z5+x
			z5 = 4-8
			u6 = z5*5
			paths.append(2)
		if z5 > 3:
			x = 5+x
			x = z5+6
			u6 = u6-6
			paths.append(3)
		else:
			u6 = u6*u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))