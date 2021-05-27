import numpy as np 

def function(x):

	b7 = 5
	h0 = 8
	paths = []
	try:
		if x >= 3:
			b7 = 5/x
			h0 = h0/3
			paths.append(1)
		else:
			h0 = 5/1
			paths.append(2)
		if h0 <= 4:
			x = x/h0
			x = x+4
			paths.append(3)
		else:
			h0 = h0/6
			x = h0+x
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