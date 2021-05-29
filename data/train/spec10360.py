import numpy as np 

def function(x):

	y3 = x
	z5 = 5
	paths = []
	try:
		if z5 > 0:
			y3 = y3*8
			z5 = y3+x
			x = z5-4
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if z5 < 7:
			z5 = z5-6
			paths.append(3)
		else:
			z5 = z5/5
			z5 = 8/9
			y3 = y3+7
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		z5 = z5**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))