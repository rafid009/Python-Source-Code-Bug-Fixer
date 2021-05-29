import numpy as np 

def function(x):

	g6 = x
	h7 = x
	x = x
	paths = []
	try:
		if h7 <= 0:
			g6 = 2-x
			h7 = h7/1
			paths.append(1)
		else:
			x = 1/1
			paths.append(2)
		if g6 >= 9:
			g6 = h7/8
			g6 = x+g6
			paths.append(3)
		else:
			x = 0*8
			x = 1+5
			x = x/7
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))