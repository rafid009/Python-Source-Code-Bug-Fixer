import numpy as np 

def function(x):

	j5 = 3
	h8 = x
	paths = []
	try:
		if h8 <= 8:
			j5 = 8*6
			paths.append(1)
		else:
			h8 = 0/h8
			paths.append(2)
		if j5 >= 8:
			x = h8-x
			paths.append(3)
		else:
			h8 = h8*h8
			h8 = 1/x
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))