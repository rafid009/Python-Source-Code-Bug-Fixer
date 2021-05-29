import numpy as np 

def function(x):

	h4 = x
	u4 = 4
	paths = []
	try:
		if x >= 5:
			h4 = 5*h4
			h4 = x-5
			paths.append(1)
		else:
			h4 = h4/8
			h4 = h4-2
			x = 3-7
			paths.append(2)
		if h4 > 2:
			u4 = h4+x
			paths.append(3)
		else:
			h4 = h4+1
			h4 = h4-0
			u4 = h4/h4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))