import numpy as np 

def function(x):

	h0 = x
	x0 = x
	paths = []
	try:
		if x0 >= 6:
			h0 = 9+4
			paths.append(1)
		else:
			h0 = x+2
			x0 = 2+2
			paths.append(2)
		if h0 <= 5:
			h0 = 7/h0
			paths.append(3)
		else:
			x0 = x/x0
			x0 = 4*2
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))