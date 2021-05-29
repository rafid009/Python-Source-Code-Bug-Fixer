import numpy as np 

def function(x):

	y0 = 6
	z7 = x
	paths = []
	try:
		if y0 <= 8:
			z7 = z7/1
			z7 = z7+5
			y0 = 0-y0
			paths.append(1)
		else:
			z7 = 1*z7
			x = 1*y0
			paths.append(2)
		if z7 >= 9:
			z7 = 0+4
			x = x*5
			x = x*9
			paths.append(3)
		else:
			z7 = 5-x
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y0 = x**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))