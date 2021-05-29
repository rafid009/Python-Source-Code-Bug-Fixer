import numpy as np 

def function(x):

	h6 = 6
	u5 = x
	paths = []
	try:
		if u5 <= 4:
			x = x/4
			x = 9*h6
			h6 = u5+0
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if h6 <= 1:
			u5 = u5/7
			h6 = h6*u5
			paths.append(3)
		else:
			h6 = u5-u5
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		h6 = u5**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))