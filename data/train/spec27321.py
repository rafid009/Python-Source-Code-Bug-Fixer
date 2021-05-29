import numpy as np 

def function(x):

	g2 = 7
	h3 = x
	paths = []
	try:
		if g2 < 0:
			g2 = g2+g2
			h3 = h3/x
			g2 = g2+3
			paths.append(1)
		else:
			h3 = h3*9
			g2 = h3/g2
			paths.append(2)
		if h3 <= 7:
			g2 = g2*7
			x = x*g2
			x = h3*2
			paths.append(3)
		else:
			g2 = g2*1
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