import numpy as np 

def function(x):

	h9 = x
	j5 = 7
	paths = []
	try:
		if j5 >= 5:
			j5 = 2/j5
			paths.append(1)
		else:
			h9 = h9-j5
			h9 = 5-7
			j5 = 4*4
			paths.append(2)
		if j5 < 4:
			j5 = j5+j5
			h9 = x-h9
			j5 = j5-x
			paths.append(3)
		else:
			x = x*8
			x = x-2
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