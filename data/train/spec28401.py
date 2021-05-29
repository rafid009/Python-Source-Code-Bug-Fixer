import numpy as np 

def function(x):

	z1 = 1
	y3 = 8
	paths = []
	try:
		if x < 4:
			z1 = z1-9
			y3 = y3+7
			paths.append(1)
		else:
			x = x*7
			z1 = z1*3
			paths.append(2)
		if x <= 0:
			y3 = z1/y3
			x = x-6
			paths.append(3)
		else:
			z1 = z1/7
			z1 = 0-5
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