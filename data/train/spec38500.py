import numpy as np 

def function(x):

	g2 = 2
	o3 = 0
	paths = []
	try:
		if x < 1:
			g2 = 5*x
			paths.append(1)
		else:
			x = 8*6
			g2 = g2-o3
			g2 = 7-o3
			paths.append(2)
		if g2 > 5:
			g2 = o3+2
			paths.append(3)
		else:
			x = o3-x
			g2 = g2+0
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