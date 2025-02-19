import numpy as np 

def function(x):

	g1 = x
	h5 = x
	paths = []
	try:
		if h5 >= 3:
			x = g1/8
			paths.append(1)
		else:
			g1 = h5/5
			paths.append(2)
		if g1 < 2:
			g1 = 4-1
			x = g1/h5
			h5 = 3+2
			paths.append(3)
		else:
			h5 = 0+h5
			h5 = 1-7
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		g1 = h5**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))