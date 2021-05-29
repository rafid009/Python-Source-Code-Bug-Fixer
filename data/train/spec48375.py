import numpy as np 

def function(x):

	x8 = 0
	h0 = x
	paths = []
	try:
		if x <= 3:
			h0 = h0-9
			paths.append(1)
		else:
			h0 = 0*2
			paths.append(2)
		if x8 >= 7:
			h0 = h0/6
			x8 = 2*1
			paths.append(3)
		else:
			x = x*6
			x = 0+x
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