import numpy as np 

def function(x):

	g5 = x
	h1 = x
	paths = []
	try:
		if g5 >= 0:
			x = h1/h1
			x = 7/4
			h1 = 0/g5
			paths.append(1)
		else:
			g5 = g5+9
			g5 = g5-h1
			g5 = g5+7
			paths.append(2)
		if h1 <= 6:
			x = x+3
			paths.append(3)
		else:
			x = 7+8
			g5 = g5+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))