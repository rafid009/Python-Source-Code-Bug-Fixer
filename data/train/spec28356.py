import numpy as np 

def function(x):

	j3 = x
	h6 = x
	paths = []
	try:
		if j3 < 4:
			x = x*6
			x = 8+1
			paths.append(1)
		else:
			x = 4*8
			paths.append(2)
		if x >= 1:
			h6 = h6-3
			x = 2-7
			h6 = 8/j3
			paths.append(3)
		else:
			j3 = j3+8
			j3 = 6+j3
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))