import numpy as np 

def function(x):

	e4 = 8
	h0 = 5
	paths = []
	try:
		if x > 8:
			e4 = x/e4
			x = 2*1
			paths.append(1)
		else:
			h0 = e4-2
			paths.append(2)
		if x < 3:
			h0 = 4-2
			e4 = 1/x
			e4 = x+5
			paths.append(3)
		else:
			e4 = 1+e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		h0 = e4**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))