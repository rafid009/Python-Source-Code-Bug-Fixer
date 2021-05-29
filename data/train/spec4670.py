import numpy as np 

def function(x):

	l3 = 9
	h0 = x
	paths = []
	try:
		if l3 < 0:
			l3 = x-x
			h0 = h0/5
			h0 = h0/1
			paths.append(1)
		else:
			x = x+h0
			l3 = l3/l3
			paths.append(2)
		if h0 > 5:
			l3 = x-l3
			paths.append(3)
		else:
			l3 = 9/5
			h0 = h0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))