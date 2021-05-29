import numpy as np 

def function(x):

	z4 = x
	y4 = 0
	paths = []
	try:
		if x <= 7:
			x = x+x
			paths.append(1)
		else:
			z4 = 6/z4
			x = 3*x
			y4 = 2+2
			paths.append(2)
		if x < 1:
			y4 = 8+4
			z4 = 8*z4
			paths.append(3)
		else:
			y4 = y4-4
			x = 2/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))