import numpy as np 

def function(x):

	g7 = x
	h0 = 2
	paths = []
	try:
		if x >= 1:
			x = 1/x
			h0 = 6+7
			paths.append(1)
		else:
			g7 = x-6
			h0 = 6+h0
			paths.append(2)
		if g7 >= 9:
			x = x/6
			g7 = g7-8
			g7 = g7/x
			paths.append(3)
		else:
			g7 = g7*h0
			x = x*2
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		h0 = g7**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))