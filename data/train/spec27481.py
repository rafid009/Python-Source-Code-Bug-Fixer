import numpy as np 

def function(x):

	h0 = x
	g3 = x
	paths = []
	try:
		if x <= 3:
			g3 = g3/h0
			g3 = g3*8
			paths.append(1)
		else:
			g3 = x*g3
			h0 = h0/h0
			g3 = g3+h0
			paths.append(2)
		if x < 6:
			g3 = 8*g3
			h0 = x*4
			paths.append(3)
		else:
			h0 = 5/h0
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