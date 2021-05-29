import numpy as np 

def function(x):

	h3 = 0
	k1 = 0
	paths = []
	try:
		if x > 7:
			x = k1*6
			k1 = k1-7
			paths.append(1)
		else:
			x = x-9
			k1 = h3*k1
			paths.append(2)
		if h3 >= 2:
			k1 = 2-2
			paths.append(3)
		else:
			x = x+8
			h3 = 8-h3
			h3 = 4-8
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		h3 = k1**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))