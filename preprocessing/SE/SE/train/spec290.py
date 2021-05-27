import numpy as np 

def function(x):

	h9 = 3
	g2 = 5
	paths = []
	try:
		if g2 > 8:
			x = x-0
			h9 = 4*h9
			g2 = 0/g2
			paths.append(1)
		else:
			x = 8+x
			h9 = h9+3
			g2 = h9-9
			paths.append(2)
		if g2 > 8:
			h9 = 9*1
			paths.append(3)
		else:
			h9 = 7*x
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