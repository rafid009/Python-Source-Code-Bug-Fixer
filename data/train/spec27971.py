import numpy as np 

def function(x):

	k4 = x
	h4 = x
	paths = []
	try:
		if h4 >= 5:
			h4 = 9*2
			paths.append(1)
		else:
			x = x/1
			k4 = k4/1
			paths.append(2)
		if k4 >= 2:
			k4 = 3-k4
			h4 = 0+h4
			k4 = k4*k4
			paths.append(3)
		else:
			h4 = h4*5
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		h4 = h4**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))