import numpy as np 

def function(x):

	h0 = x
	u2 = 9
	paths = []
	try:
		if x <= 9:
			h0 = h0*5
			x = 9*x
			u2 = h0+7
			paths.append(1)
		else:
			x = 3+u2
			u2 = u2*x
			h0 = 5-h0
			paths.append(2)
		if x <= 9:
			h0 = h0-0
			h0 = h0+h0
			x = 1/x
			paths.append(3)
		else:
			h0 = 8/u2
			x = x/2
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		u2 = h0**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))