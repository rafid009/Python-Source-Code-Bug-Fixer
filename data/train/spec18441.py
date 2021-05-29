import numpy as np 

def function(x):

	h3 = 8
	u6 = 8
	paths = []
	try:
		if u6 >= 2:
			h3 = 7-h3
			x = x-8
			paths.append(1)
		else:
			u6 = 5*u6
			x = 6-h3
			u6 = h3+u6
			paths.append(2)
		if h3 >= 2:
			u6 = 5*u6
			x = 8*2
			u6 = h3/u6
			paths.append(3)
		else:
			u6 = 6+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))