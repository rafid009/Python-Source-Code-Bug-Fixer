import numpy as np 

def function(x):

	u9 = 7
	h9 = 4
	paths = []
	try:
		if u9 > 8:
			u9 = 2+u9
			h9 = 8-x
			paths.append(1)
		else:
			x = x*3
			u9 = x-u9
			paths.append(2)
		if u9 >= 2:
			x = x+5
			u9 = u9-6
			u9 = 1+u9
			paths.append(3)
		else:
			h9 = h9-6
			u9 = 8/u9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))