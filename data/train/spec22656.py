import numpy as np 

def function(x):

	a7 = x
	g2 = x
	paths = []
	try:
		if g2 < 5:
			g2 = g2*7
			paths.append(1)
		else:
			a7 = a7+9
			a7 = 4-a7
			paths.append(2)
		if g2 < 2:
			x = 9+g2
			x = x-5
			paths.append(3)
		else:
			g2 = g2-1
			x = 7*2
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