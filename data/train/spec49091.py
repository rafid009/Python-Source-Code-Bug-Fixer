import numpy as np 

def function(x):

	l4 = x
	h0 = 8
	paths = []
	try:
		if l4 >= 2:
			h0 = l4-4
			l4 = 3-x
			paths.append(1)
		else:
			h0 = 7/x
			l4 = x*l4
			x = l4*8
			paths.append(2)
		if h0 > 5:
			x = x+h0
			h0 = h0+2
			paths.append(3)
		else:
			l4 = h0/l4
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		h0 = l4**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))