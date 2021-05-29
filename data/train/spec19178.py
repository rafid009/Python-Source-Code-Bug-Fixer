import numpy as np 

def function(x):

	h0 = x
	l9 = 4
	paths = []
	try:
		if x >= 5:
			x = 4-l9
			x = h0+l9
			h0 = h0*0
			paths.append(1)
		else:
			h0 = h0/2
			l9 = l9+6
			l9 = 6-l9
			paths.append(2)
		if x <= 1:
			h0 = 1/h0
			x = x*1
			paths.append(3)
		else:
			x = x/8
			x = l9-x
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