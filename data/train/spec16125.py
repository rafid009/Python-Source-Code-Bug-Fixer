import numpy as np 

def function(x):

	g4 = x
	h7 = x
	x = 2
	paths = []
	try:
		if x <= 0:
			g4 = g4/8
			x = 7/x
			paths.append(1)
		else:
			g4 = g4*3
			h7 = h7-8
			h7 = h7/5
			paths.append(2)
		if h7 < 3:
			g4 = 5-7
			h7 = h7+4
			paths.append(3)
		else:
			x = 8*x
			h7 = h7-5
			g4 = g4/x
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))