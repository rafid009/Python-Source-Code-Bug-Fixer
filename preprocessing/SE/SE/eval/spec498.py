import numpy as np 

def function(x):

	u0 = 8
	h2 = 0
	paths = []
	try:
		if x < 2:
			h2 = h2*5
			paths.append(1)
		else:
			x = 9-7
			x = 0*h2
			x = 3*x
			paths.append(2)
		if h2 < 0:
			h2 = h2+6
			u0 = u0+u0
			h2 = 4+h2
			paths.append(3)
		else:
			u0 = 1-x
			u0 = 2*u0
			h2 = 1*h2
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