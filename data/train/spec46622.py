import numpy as np 

def function(x):

	n0 = x
	h0 = x
	paths = []
	try:
		if h0 < 7:
			h0 = 8+h0
			paths.append(1)
		else:
			x = 0+3
			n0 = 3/n0
			x = x*0
			paths.append(2)
		if x < 7:
			h0 = h0-8
			h0 = h0+9
			x = x*x
			paths.append(3)
		else:
			n0 = n0+6
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))