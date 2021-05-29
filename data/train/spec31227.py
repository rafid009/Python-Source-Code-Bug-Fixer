import numpy as np 

def function(x):

	h7 = 4
	u7 = 4
	paths = []
	try:
		if u7 <= 1:
			u7 = h7*u7
			h7 = 6-5
			x = x*6
			paths.append(1)
		else:
			x = 2-h7
			h7 = 6/h7
			paths.append(2)
		if u7 > 6:
			h7 = 0/h7
			u7 = h7*u7
			paths.append(3)
		else:
			x = 6/x
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))