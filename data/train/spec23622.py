import numpy as np 

def function(x):

	h0 = 8
	u4 = 5
	paths = []
	try:
		if h0 >= 9:
			h0 = h0/u4
			paths.append(1)
		else:
			h0 = 0+h0
			h0 = h0-x
			paths.append(2)
		if x <= 0:
			h0 = h0/1
			x = 3+x
			paths.append(3)
		else:
			x = 1*x
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