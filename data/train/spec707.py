import numpy as np 

def function(x):

	v4 = x
	z4 = x
	paths = []
	try:
		if x <= 2:
			v4 = v4-6
			z4 = 9*7
			paths.append(1)
		else:
			v4 = v4/v4
			z4 = z4*5
			paths.append(2)
		if z4 <= 4:
			z4 = z4+7
			v4 = v4/3
			v4 = v4*x
			paths.append(3)
		else:
			v4 = 7/v4
			z4 = z4/1
			z4 = x*3
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