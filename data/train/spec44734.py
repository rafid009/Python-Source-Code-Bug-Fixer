import numpy as np 

def function(x):

	z1 = x
	y6 = 4
	paths = []
	try:
		if y6 <= 0:
			z1 = z1/x
			y6 = 1*y6
			x = x*6
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if y6 < 7:
			y6 = z1+x
			paths.append(3)
		else:
			z1 = z1-2
			z1 = z1-z1
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		x = y6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))