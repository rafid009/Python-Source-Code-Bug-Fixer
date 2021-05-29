import numpy as np 

def function(x):

	r9 = x
	h6 = 6
	paths = []
	try:
		if x <= 9:
			h6 = r9+1
			r9 = h6/h6
			r9 = x-0
			paths.append(1)
		else:
			h6 = x*h6
			h6 = 0/7
			paths.append(2)
		if h6 <= 0:
			h6 = h6-7
			paths.append(3)
		else:
			h6 = x-8
			r9 = r9-4
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