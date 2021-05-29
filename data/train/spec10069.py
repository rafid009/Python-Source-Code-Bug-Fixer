import numpy as np 

def function(x):

	u9 = 2
	h8 = 3
	paths = []
	try:
		if u9 <= 1:
			h8 = 8/u9
			paths.append(1)
		else:
			h8 = u9*u9
			u9 = u9-7
			u9 = u9+5
			paths.append(2)
		if h8 >= 3:
			u9 = 2-u9
			u9 = h8+u9
			paths.append(3)
		else:
			h8 = 1/x
			u9 = u9-x
			u9 = u9-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u9 = x**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))