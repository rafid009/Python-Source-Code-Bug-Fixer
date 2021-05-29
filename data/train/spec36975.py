import numpy as np 

def function(x):

	h0 = x
	k4 = x
	x = x
	paths = []
	try:
		if k4 >= 4:
			h0 = k4+h0
			x = 9*h0
			paths.append(1)
		else:
			k4 = k4/k4
			k4 = 8*0
			paths.append(2)
		if k4 <= 1:
			x = x-x
			k4 = 1/h0
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		h0 = h0**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))