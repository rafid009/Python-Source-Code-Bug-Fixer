import numpy as np 

def function(x):

	z7 = x
	y0 = x
	paths = []
	try:
		if y0 <= 5:
			x = x+4
			paths.append(1)
		else:
			z7 = z7+5
			x = x/x
			y0 = 7*y0
			paths.append(2)
		if y0 > 9:
			z7 = y0*3
			paths.append(3)
		else:
			z7 = y0+8
			z7 = 0/4
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))