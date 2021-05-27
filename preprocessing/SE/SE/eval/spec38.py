import numpy as np 

def function(x):

	h0 = 1
	f2 = x
	paths = []
	try:
		if h0 < 4:
			h0 = x-7
			x = 4+8
			paths.append(1)
		else:
			f2 = h0*3
			h0 = h0*h0
			paths.append(2)
		if x <= 0:
			f2 = h0/4
			h0 = h0+8
			paths.append(3)
		else:
			f2 = 9-f2
			x = 1*x
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