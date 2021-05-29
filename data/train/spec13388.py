import numpy as np 

def function(x):

	g2 = 0
	n9 = 4
	paths = []
	try:
		if x < 7:
			g2 = 0*g2
			g2 = n9-3
			paths.append(1)
		else:
			n9 = x*x
			n9 = n9-n9
			paths.append(2)
		if x >= 0:
			g2 = 3-g2
			paths.append(3)
		else:
			n9 = g2+g2
			n9 = n9+9
			n9 = n9/g2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g2 = x**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))