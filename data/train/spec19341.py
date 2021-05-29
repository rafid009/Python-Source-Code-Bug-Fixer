import numpy as np 

def function(x):

	g2 = x
	g4 = 7
	paths = []
	try:
		if g2 <= 1:
			g2 = 1+g4
			paths.append(1)
		else:
			g2 = 5-g2
			g2 = g4+3
			paths.append(2)
		if g2 <= 7:
			g4 = 3-1
			g2 = g2*7
			g4 = 3+9
			paths.append(3)
		else:
			g4 = 8/g2
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