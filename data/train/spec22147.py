import numpy as np 

def function(x):

	h0 = 4
	f4 = 8
	x = x
	paths = []
	try:
		if x >= 7:
			h0 = h0/h0
			paths.append(1)
		else:
			f4 = 8/x
			h0 = h0+h0
			paths.append(2)
		if f4 > 9:
			f4 = f4-6
			h0 = h0*6
			paths.append(3)
		else:
			h0 = h0/7
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