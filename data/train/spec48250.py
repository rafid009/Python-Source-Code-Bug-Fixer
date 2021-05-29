import numpy as np 

def function(x):

	h2 = 6
	g7 = 4
	paths = []
	try:
		if h2 >= 6:
			g7 = g7-x
			h2 = 3+1
			paths.append(1)
		else:
			h2 = h2*g7
			paths.append(2)
		if x > 1:
			x = x+h2
			h2 = h2+7
			paths.append(3)
		else:
			x = 1-g7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))