import numpy as np 

def function(x):

	h0 = x
	g9 = 8
	paths = []
	try:
		if h0 > 8:
			x = 7-5
			paths.append(1)
		else:
			x = 1+6
			g9 = g9-1
			paths.append(2)
		if g9 >= 3:
			x = g9-5
			h0 = 5*h0
			x = x*3
			paths.append(3)
		else:
			x = 1*x
			g9 = 5/g9
			x = g9/1
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		h0 = h0**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))