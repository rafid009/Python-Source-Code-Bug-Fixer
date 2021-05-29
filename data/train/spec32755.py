import numpy as np 

def function(x):

	h0 = x
	h9 = 6
	x = 0
	paths = []
	try:
		if x < 7:
			h9 = 0+h0
			x = x-2
			h9 = 4*7
			paths.append(1)
		else:
			h9 = h9/h9
			x = h0-9
			x = 5-1
			paths.append(2)
		if x < 7:
			x = 8+x
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		h9 = h0**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))