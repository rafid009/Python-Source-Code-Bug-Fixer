import numpy as np 

def function(x):

	g2 = 7
	d3 = 5
	x = x
	paths = []
	try:
		if x > 3:
			x = x*9
			paths.append(1)
		else:
			g2 = g2*d3
			g2 = 0*5
			paths.append(2)
		if g2 < 0:
			x = x/g2
			x = d3-3
			paths.append(3)
		else:
			d3 = d3+8
			x = x+3
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