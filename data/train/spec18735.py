import numpy as np 

def function(x):

	h1 = x
	g9 = 9
	paths = []
	try:
		if x > 9:
			h1 = g9/h1
			h1 = 7+h1
			paths.append(1)
		else:
			x = g9*h1
			h1 = h1*h1
			x = 7-2
			paths.append(2)
		if g9 <= 0:
			x = h1/7
			h1 = 2*h1
			g9 = 8-4
			paths.append(3)
		else:
			g9 = 3*h1
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))