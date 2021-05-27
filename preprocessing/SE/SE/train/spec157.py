import numpy as np 

def function(x):

	h0 = x
	l4 = x
	paths = []
	try:
		if l4 > 5:
			l4 = 5-2
			l4 = l4*5
			paths.append(1)
		else:
			l4 = 3*l4
			paths.append(2)
		if h0 <= 2:
			l4 = x/x
			x = x/7
			paths.append(3)
		else:
			h0 = 0-4
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