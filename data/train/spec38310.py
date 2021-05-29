import numpy as np 

def function(x):

	h8 = 3
	q1 = 8
	paths = []
	try:
		if h8 < 1:
			h8 = h8-h8
			paths.append(1)
		else:
			h8 = h8*7
			paths.append(2)
		if x < 5:
			h8 = 8-h8
			paths.append(3)
		else:
			q1 = q1+h8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		q1 = h8**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))