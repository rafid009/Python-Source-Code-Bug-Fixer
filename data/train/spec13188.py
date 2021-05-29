import numpy as np 

def function(x):

	z1 = x
	g2 = 9
	paths = []
	try:
		if g2 <= 8:
			x = 5*x
			paths.append(1)
		else:
			g2 = g2+3
			x = x-g2
			z1 = g2-z1
			paths.append(2)
		if g2 <= 9:
			x = g2*x
			g2 = z1-9
			g2 = 2*g2
			paths.append(3)
		else:
			g2 = g2*3
			x = z1-0
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))