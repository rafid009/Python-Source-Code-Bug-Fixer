import numpy as np 

def function(x):

	g8 = x
	z4 = 8
	x = 2
	paths = []
	try:
		if z4 < 0:
			x = 8/3
			paths.append(1)
		else:
			z4 = 1/4
			z4 = x/7
			z4 = g8/z4
			paths.append(2)
		if x <= 4:
			z4 = 8+z4
			paths.append(3)
		else:
			x = z4*z4
			z4 = z4-9
			g8 = 3/6
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))