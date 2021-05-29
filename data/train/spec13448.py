import numpy as np 

def function(x):

	g2 = x
	d5 = x
	paths = []
	try:
		if d5 < 5:
			g2 = g2+3
			g2 = 2+g2
			paths.append(1)
		else:
			g2 = x+8
			paths.append(2)
		if d5 < 5:
			g2 = g2-6
			paths.append(3)
		else:
			d5 = 5/2
			g2 = 7/g2
			x = x/8
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