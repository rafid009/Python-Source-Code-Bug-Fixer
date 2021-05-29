import numpy as np 

def function(x):

	h3 = x
	g6 = x
	paths = []
	try:
		if g6 > 9:
			h3 = 1-h3
			x = 1-h3
			h3 = h3/7
			paths.append(1)
		else:
			h3 = 1*1
			paths.append(2)
		if g6 <= 2:
			h3 = 9*0
			paths.append(3)
		else:
			g6 = 3/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))