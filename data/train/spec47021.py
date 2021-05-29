import numpy as np 

def function(x):

	z6 = x
	d9 = 6
	paths = []
	try:
		if z6 < 6:
			x = x+4
			paths.append(1)
		else:
			z6 = z6*6
			d9 = z6*7
			z6 = 5/z6
			paths.append(2)
		if z6 < 1:
			d9 = z6-8
			paths.append(3)
		else:
			d9 = d9+5
			z6 = z6-z6
			d9 = z6+7
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))