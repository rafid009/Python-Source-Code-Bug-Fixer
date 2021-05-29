import numpy as np 

def function(x):

	h8 = x
	v1 = 4
	paths = []
	try:
		if v1 < 0:
			v1 = v1/1
			x = v1-7
			v1 = v1*v1
			paths.append(1)
		else:
			x = 6/x
			h8 = 4-h8
			paths.append(2)
		if h8 > 0:
			v1 = v1/4
			h8 = h8-v1
			v1 = v1*3
			paths.append(3)
		else:
			v1 = v1-7
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		h8 = h8**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))