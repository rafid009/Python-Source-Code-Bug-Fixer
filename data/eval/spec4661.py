import numpy as np 

def function(x):

	z6 = 5
	v7 = 3
	paths = []
	try:
		if x < 8:
			z6 = z6-8
			z6 = 1/z6
			paths.append(1)
		else:
			x = 0-7
			z6 = z6*4
			paths.append(2)
		if x <= 0:
			v7 = 0+x
			paths.append(3)
		else:
			v7 = v7-3
			x = x/x
			z6 = v7-x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		z6 = v7**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))