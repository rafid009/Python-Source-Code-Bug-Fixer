import numpy as np 

def function(x):

	z2 = x
	y1 = 3
	paths = []
	try:
		if y1 < 3:
			y1 = y1-4
			z2 = z2+7
			paths.append(1)
		else:
			x = x+8
			x = 8+x
			paths.append(2)
		if z2 > 6:
			x = x-x
			x = 9*x
			paths.append(3)
		else:
			z2 = 2*z2
			z2 = 5/z2
			y1 = 1*z2
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