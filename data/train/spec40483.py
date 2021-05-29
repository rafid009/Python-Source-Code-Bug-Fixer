import numpy as np 

def function(x):

	g2 = 2
	g4 = x
	paths = []
	try:
		if g2 >= 8:
			x = 2/x
			g2 = g4/g2
			g4 = 5+x
			paths.append(1)
		else:
			x = x-2
			g4 = 5*2
			paths.append(2)
		if g2 <= 6:
			g2 = g2+x
			g2 = g2+8
			x = g4/4
			paths.append(3)
		else:
			g2 = 3-g2
			g4 = g4-3
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		g2 = g2**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))