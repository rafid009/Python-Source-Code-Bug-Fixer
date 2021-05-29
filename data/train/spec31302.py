import numpy as np 

def function(x):

	u9 = 6
	h6 = 2
	paths = []
	try:
		if u9 < 4:
			h6 = h6+4
			u9 = x*u9
			h6 = h6*0
			paths.append(1)
		else:
			h6 = 1/h6
			u9 = u9*h6
			u9 = 9+4
			paths.append(2)
		if h6 < 3:
			u9 = h6-8
			h6 = x-0
			u9 = u9-8
			paths.append(3)
		else:
			h6 = h6+u9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))