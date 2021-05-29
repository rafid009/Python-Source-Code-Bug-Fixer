import numpy as np 

def function(x):

	h8 = 6
	v0 = 1
	paths = []
	try:
		if x >= 5:
			x = x*v0
			x = 1+h8
			x = h8+x
			paths.append(1)
		else:
			x = x+0
			h8 = h8-x
			v0 = 5/x
			paths.append(2)
		if v0 >= 2:
			h8 = h8-7
			paths.append(3)
		else:
			h8 = h8*v0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))