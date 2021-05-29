import numpy as np 

def function(x):

	y1 = 0
	z5 = 2
	paths = []
	try:
		if z5 >= 7:
			y1 = x/1
			y1 = 0-y1
			y1 = z5-6
			paths.append(1)
		else:
			y1 = y1/7
			x = 7*x
			y1 = y1/5
			paths.append(2)
		if y1 < 7:
			z5 = z5*z5
			y1 = y1+2
			x = x/9
			paths.append(3)
		else:
			z5 = z5-5
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