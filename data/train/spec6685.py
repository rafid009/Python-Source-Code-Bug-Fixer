import numpy as np 

def function(x):

	h4 = 0
	g3 = 7
	paths = []
	try:
		if x < 7:
			g3 = x+g3
			paths.append(1)
		else:
			g3 = g3*h4
			g3 = 1*h4
			paths.append(2)
		if h4 >= 2:
			x = x*8
			g3 = 1*g3
			paths.append(3)
		else:
			h4 = 9*1
			h4 = x/5
			h4 = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))