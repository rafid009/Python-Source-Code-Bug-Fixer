import numpy as np 

def function(x):

	h0 = 3
	t1 = 7
	paths = []
	try:
		if t1 < 0:
			h0 = t1*6
			h0 = h0+5
			x = 5*x
			paths.append(1)
		else:
			t1 = t1-h0
			paths.append(2)
		if x < 9:
			t1 = t1/1
			h0 = 0*h0
			paths.append(3)
		else:
			h0 = h0-4
			t1 = 1+t1
			t1 = x+8
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