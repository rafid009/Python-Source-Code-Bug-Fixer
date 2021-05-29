import numpy as np 

def function(x):

	g2 = x
	c3 = 2
	paths = []
	try:
		if g2 <= 6:
			g2 = 5/c3
			c3 = c3+3
			paths.append(1)
		else:
			x = g2-3
			g2 = g2-c3
			paths.append(2)
		if c3 <= 7:
			x = x+9
			paths.append(3)
		else:
			x = x/1
			x = x/5
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