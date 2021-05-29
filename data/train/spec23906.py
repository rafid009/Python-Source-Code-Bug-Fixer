import numpy as np 

def function(x):

	h9 = 1
	q3 = 1
	paths = []
	try:
		if h9 < 5:
			q3 = 0/6
			q3 = 3*q3
			paths.append(1)
		else:
			h9 = h9-9
			x = 8*6
			paths.append(2)
		if x < 4:
			h9 = 0/h9
			paths.append(3)
		else:
			h9 = 2-9
			h9 = q3+h9
			x = x*h9
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))