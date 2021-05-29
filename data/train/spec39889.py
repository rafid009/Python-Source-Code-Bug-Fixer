import numpy as np 

def function(x):

	h3 = x
	h0 = x
	x = 1
	paths = []
	try:
		if x >= 3:
			h0 = 4*8
			h3 = 0/h3
			paths.append(1)
		else:
			x = 1/9
			paths.append(2)
		if h3 <= 5:
			x = 9+0
			x = 2-x
			paths.append(3)
		else:
			h0 = 8+h0
			h0 = 1/h3
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h0 = h3**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))