import numpy as np 

def function(x):

	i4 = 4
	h8 = 7
	x = x
	paths = []
	try:
		if x < 5:
			h8 = 9-x
			x = h8+8
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if i4 <= 6:
			i4 = 1-5
			x = i4-1
			paths.append(3)
		else:
			i4 = i4+9
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		h8 = i4**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))