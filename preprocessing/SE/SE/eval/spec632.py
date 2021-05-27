import numpy as np 

def function(x):

	z9 = 3
	y1 = x
	paths = []
	try:
		if x <= 3:
			x = x+z9
			paths.append(1)
		else:
			z9 = 3-z9
			z9 = z9+z9
			paths.append(2)
		if x >= 6:
			y1 = y1*8
			y1 = y1+3
			y1 = 0-y1
			paths.append(3)
		else:
			y1 = z9+y1
			y1 = y1/y1
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