import numpy as np 

def function(x):

	h7 = x
	u7 = 7
	paths = []
	try:
		if h7 >= 8:
			u7 = h7-4
			u7 = h7+x
			x = 1/x
			paths.append(1)
		else:
			x = u7/x
			h7 = h7-x
			paths.append(2)
		if x <= 3:
			x = x+x
			paths.append(3)
		else:
			x = 6-9
			h7 = 1/h7
			u7 = x-7
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		u7 = u7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))