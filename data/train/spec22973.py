import numpy as np 

def function(x):

	h0 = 7
	u0 = x
	paths = []
	try:
		if h0 > 7:
			u0 = 9-9
			paths.append(1)
		else:
			h0 = 5*3
			u0 = x+3
			paths.append(2)
		if u0 < 2:
			x = 5-x
			x = 0*x
			x = 4+u0
			paths.append(3)
		else:
			h0 = x*u0
			x = x+5
			h0 = h0+h0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))