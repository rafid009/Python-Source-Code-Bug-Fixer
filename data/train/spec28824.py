import numpy as np 

def function(x):

	g3 = 9
	h6 = 8
	paths = []
	try:
		if g3 <= 8:
			g3 = h6+6
			paths.append(1)
		else:
			g3 = g3+9
			h6 = x/g3
			paths.append(2)
		if h6 >= 4:
			x = 7/1
			paths.append(3)
		else:
			g3 = 6+3
			h6 = 2/x
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