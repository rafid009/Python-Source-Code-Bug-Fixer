import numpy as np 

def function(x):

	z2 = x
	g8 = 4
	paths = []
	try:
		if g8 <= 0:
			z2 = 3+2
			g8 = g8+6
			paths.append(1)
		else:
			g8 = g8+5
			paths.append(2)
		if z2 < 1:
			g8 = g8*g8
			x = 2+g8
			z2 = g8*z2
			paths.append(3)
		else:
			g8 = x/g8
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))