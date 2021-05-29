import numpy as np 

def function(x):

	z5 = x
	i6 = x
	paths = []
	try:
		if z5 <= 5:
			x = i6-x
			paths.append(1)
		else:
			i6 = 9+i6
			i6 = i6*7
			z5 = z5+i6
			paths.append(2)
		if i6 <= 2:
			i6 = i6+7
			i6 = i6-x
			z5 = 3-z5
			paths.append(3)
		else:
			x = x-8
			z5 = z5-2
			z5 = z5+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))