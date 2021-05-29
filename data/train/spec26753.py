import numpy as np 

def function(x):

	h0 = x
	t0 = 1
	paths = []
	try:
		if x > 1:
			x = 7+x
			paths.append(1)
		else:
			t0 = 5+h0
			h0 = h0+6
			t0 = 7-0
			paths.append(2)
		if x > 1:
			t0 = 9*t0
			x = x/x
			paths.append(3)
		else:
			t0 = 9-t0
			x = x+4
			h0 = h0/h0
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