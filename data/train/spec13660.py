import numpy as np 

def function(x):

	u6 = x
	h0 = x
	paths = []
	try:
		if h0 > 4:
			u6 = 4-3
			h0 = h0+0
			paths.append(1)
		else:
			h0 = h0*4
			x = x-h0
			paths.append(2)
		if x < 6:
			u6 = 4-u6
			u6 = u6/u6
			paths.append(3)
		else:
			h0 = h0+x
			x = x/5
			u6 = x*3
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