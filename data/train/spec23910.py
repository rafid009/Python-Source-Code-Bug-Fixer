import numpy as np 

def function(x):

	g7 = 6
	z1 = 9
	paths = []
	try:
		if x < 0:
			z1 = z1+3
			x = x*1
			x = 7/9
			paths.append(1)
		else:
			x = 3-x
			z1 = 2+5
			x = 6+x
			paths.append(2)
		if z1 > 1:
			z1 = z1*6
			paths.append(3)
		else:
			g7 = 7+6
			z1 = 2+z1
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))