import numpy as np 

def function(x):

	g4 = 7
	i9 = x
	paths = []
	try:
		if i9 > 3:
			x = g4*x
			g4 = 3*i9
			i9 = i9*g4
			paths.append(1)
		else:
			x = x+x
			g4 = i9+5
			paths.append(2)
		if i9 < 9:
			i9 = i9/9
			x = g4-5
			paths.append(3)
		else:
			x = x+x
			g4 = i9-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))