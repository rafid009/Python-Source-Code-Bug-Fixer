import numpy as np 

def function(x):

	h0 = x
	w1 = 3
	paths = []
	try:
		if x < 6:
			x = 9*3
			paths.append(1)
		else:
			h0 = h0-h0
			w1 = 9*w1
			paths.append(2)
		if x > 5:
			h0 = h0*6
			w1 = 4*w1
			paths.append(3)
		else:
			h0 = h0+0
			w1 = x+x
			h0 = 4*h0
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