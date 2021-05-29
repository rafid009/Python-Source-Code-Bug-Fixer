import numpy as np 

def function(x):

	z4 = x
	u6 = 4
	paths = []
	try:
		if z4 >= 5:
			u6 = z4/u6
			z4 = z4*9
			paths.append(1)
		else:
			z4 = 6*z4
			paths.append(2)
		if u6 > 2:
			z4 = z4-z4
			paths.append(3)
		else:
			u6 = u6-3
			u6 = u6-u6
			z4 = 1*z4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))