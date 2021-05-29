import numpy as np 

def function(x):

	y6 = 6
	z2 = x
	paths = []
	try:
		if x > 6:
			x = y6-8
			z2 = z2/z2
			y6 = 1*z2
			paths.append(1)
		else:
			x = 8/z2
			paths.append(2)
		if y6 <= 3:
			z2 = 0-9
			y6 = y6*4
			y6 = 7+5
			paths.append(3)
		else:
			y6 = x-y6
			x = x/5
			x = x+z2
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		z2 = y6**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))