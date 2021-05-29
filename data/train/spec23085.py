import numpy as np 

def function(x):

	z2 = 8
	y3 = 2
	x = x
	paths = []
	try:
		if z2 <= 9:
			z2 = x/z2
			x = x-4
			z2 = 1-z2
			paths.append(1)
		else:
			y3 = y3*5
			z2 = 0/3
			y3 = y3/y3
			paths.append(2)
		if y3 > 6:
			z2 = 1*x
			y3 = 1*0
			x = 0-x
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		y3 = z2**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))