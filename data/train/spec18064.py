import numpy as np 

def function(x):

	h0 = x
	u0 = x
	paths = []
	try:
		if u0 >= 0:
			u0 = u0+8
			paths.append(1)
		else:
			x = 2*x
			u0 = u0/x
			paths.append(2)
		if u0 < 0:
			x = 6+x
			paths.append(3)
		else:
			u0 = u0-x
			h0 = 7+h0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))