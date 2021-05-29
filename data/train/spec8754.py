import numpy as np 

def function(x):

	h0 = x
	a7 = x
	paths = []
	try:
		if a7 >= 0:
			x = x*7
			paths.append(1)
		else:
			h0 = 2*8
			h0 = h0+a7
			paths.append(2)
		if a7 < 4:
			x = 4/6
			x = x/x
			paths.append(3)
		else:
			h0 = 7+7
			x = x-0
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		h0 = a7**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))