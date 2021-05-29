import numpy as np 

def function(x):

	i4 = 9
	h7 = 9
	paths = []
	try:
		if x <= 3:
			i4 = i4+h7
			paths.append(1)
		else:
			h7 = x*h7
			paths.append(2)
		if i4 < 5:
			x = h7-1
			h7 = 7*5
			paths.append(3)
		else:
			i4 = x-3
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		h7 = i4**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))