import numpy as np 

def function(x):

	h6 = x
	g0 = 9
	paths = []
	try:
		if h6 >= 6:
			x = x/h6
			g0 = g0/9
			paths.append(1)
		else:
			g0 = x-0
			x = 5-x
			paths.append(2)
		if h6 > 1:
			x = 1*x
			h6 = h6-h6
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		g0 = h6**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))