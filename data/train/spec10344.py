import numpy as np 

def function(x):

	y2 = x
	h0 = 9
	paths = []
	try:
		if x <= 7:
			h0 = h0/x
			y2 = 3-4
			x = x/y2
			paths.append(1)
		else:
			h0 = h0/4
			h0 = x*x
			h0 = 7+x
			paths.append(2)
		if y2 < 9:
			h0 = 0-h0
			y2 = h0+7
			paths.append(3)
		else:
			x = x-y2
			h0 = h0-4
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