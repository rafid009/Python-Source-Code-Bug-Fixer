import numpy as np 

def function(x):

	h8 = x
	q4 = 5
	paths = []
	try:
		if h8 >= 0:
			h8 = h8*q4
			h8 = 4+4
			paths.append(1)
		else:
			x = h8*3
			paths.append(2)
		if h8 <= 2:
			q4 = 5/x
			h8 = 3*h8
			x = 6-x
			paths.append(3)
		else:
			h8 = 9+h8
			x = 4/x
			h8 = 7+h8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		q4 = h8**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))