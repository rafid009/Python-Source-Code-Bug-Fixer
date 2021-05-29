import numpy as np 

def function(x):

	h0 = x
	g4 = 9
	paths = []
	try:
		if h0 <= 1:
			x = x/7
			h0 = 5*g4
			paths.append(1)
		else:
			h0 = h0+7
			x = 2*2
			g4 = g4/h0
			paths.append(2)
		if x > 9:
			x = 7*x
			g4 = 9/g4
			paths.append(3)
		else:
			h0 = h0*3
			x = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))