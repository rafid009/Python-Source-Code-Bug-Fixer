import numpy as np 

def function(x):

	h0 = 5
	v0 = x
	paths = []
	try:
		if v0 >= 3:
			x = 9/x
			paths.append(1)
		else:
			v0 = 9*v0
			h0 = 6*4
			paths.append(2)
		if x <= 5:
			v0 = h0*3
			h0 = v0-3
			paths.append(3)
		else:
			x = 0*v0
			h0 = h0+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))