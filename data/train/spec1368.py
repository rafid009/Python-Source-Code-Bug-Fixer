import numpy as np 

def function(x):

	h8 = x
	u0 = 2
	paths = []
	try:
		if u0 < 1:
			x = x/x
			paths.append(1)
		else:
			x = u0-x
			paths.append(2)
		if x >= 8:
			u0 = u0*u0
			h8 = 3*h8
			paths.append(3)
		else:
			u0 = u0+u0
			h8 = h8+4
			u0 = h8*5
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))