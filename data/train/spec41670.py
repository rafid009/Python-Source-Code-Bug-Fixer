import numpy as np 

def function(x):

	z1 = 2
	g8 = 7
	paths = []
	try:
		if z1 <= 1:
			z1 = z1-2
			x = 0*x
			paths.append(1)
		else:
			g8 = 6+6
			paths.append(2)
		if x >= 2:
			g8 = 2/2
			g8 = 7-x
			paths.append(3)
		else:
			g8 = 1/g8
			g8 = 2*g8
			x = 0-z1
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