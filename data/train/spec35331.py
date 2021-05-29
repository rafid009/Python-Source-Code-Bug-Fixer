import numpy as np 

def function(x):

	i5 = 0
	h6 = x
	paths = []
	try:
		if x >= 0:
			h6 = 3*1
			h6 = i5+h6
			x = 8*x
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if h6 > 5:
			i5 = 2-i5
			x = 5-x
			paths.append(3)
		else:
			x = 1/x
			i5 = h6-i5
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))