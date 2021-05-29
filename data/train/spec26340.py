import numpy as np 

def function(x):

	g8 = 3
	z7 = 2
	paths = []
	try:
		if x > 5:
			z7 = z7/g8
			paths.append(1)
		else:
			g8 = x/5
			g8 = 4*g8
			paths.append(2)
		if g8 < 3:
			x = z7*z7
			g8 = 1-g8
			paths.append(3)
		else:
			z7 = z7*z7
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))