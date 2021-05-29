import numpy as np 

def function(x):

	z5 = 2
	y1 = 4
	paths = []
	try:
		if y1 > 6:
			z5 = 0+x
			paths.append(1)
		else:
			z5 = y1-z5
			z5 = 7+z5
			y1 = y1*z5
			paths.append(2)
		if z5 < 5:
			z5 = 4/z5
			z5 = z5+z5
			paths.append(3)
		else:
			z5 = 2*1
			y1 = x-9
			x = x-y1
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))