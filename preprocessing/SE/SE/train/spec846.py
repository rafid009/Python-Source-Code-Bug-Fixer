import numpy as np 

def function(x):

	g6 = x
	v0 = x
	x = x
	paths = []
	try:
		if v0 <= 3:
			x = x+g6
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if x > 5:
			g6 = g6+5
			v0 = v0/4
			g6 = g6/7
			paths.append(3)
		else:
			g6 = g6*g6
			x = g6-5
			g6 = g6*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g6 = x**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))