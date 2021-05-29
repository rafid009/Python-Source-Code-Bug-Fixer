import numpy as np 

def function(x):

	d1 = x
	z6 = x
	paths = []
	try:
		if z6 >= 6:
			d1 = 8+x
			paths.append(1)
		else:
			x = z6*x
			z6 = z6*4
			paths.append(2)
		if d1 > 5:
			x = d1/8
			paths.append(3)
		else:
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))