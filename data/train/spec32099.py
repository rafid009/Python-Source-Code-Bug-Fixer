import numpy as np 

def function(x):

	h0 = 5
	o3 = 3
	paths = []
	try:
		if o3 < 5:
			h0 = h0-9
			paths.append(1)
		else:
			x = 8/x
			x = x*4
			paths.append(2)
		if o3 <= 3:
			h0 = o3+h0
			h0 = h0-o3
			paths.append(3)
		else:
			o3 = 3/o3
			h0 = 2*6
			o3 = o3+0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))