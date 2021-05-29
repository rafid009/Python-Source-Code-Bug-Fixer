import numpy as np 

def function(x):

	q3 = x
	h9 = 4
	paths = []
	try:
		if x >= 1:
			h9 = h9/8
			paths.append(1)
		else:
			h9 = h9-x
			q3 = q3*h9
			h9 = h9-1
			paths.append(2)
		if x <= 0:
			h9 = h9*h9
			paths.append(3)
		else:
			x = x/4
			h9 = 8+h9
			h9 = h9*8
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))