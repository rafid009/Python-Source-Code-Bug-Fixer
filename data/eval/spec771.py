import numpy as np 

def function(x):

	h3 = x
	g7 = x
	paths = []
	try:
		if h3 > 2:
			h3 = h3*4
			x = x+x
			paths.append(1)
		else:
			h3 = 3/x
			g7 = 0/7
			x = x/x
			paths.append(2)
		if x > 1:
			g7 = g7-x
			paths.append(3)
		else:
			g7 = h3/2
			x = 0/x
			h3 = 4/h3
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))