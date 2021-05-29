import numpy as np 

def function(x):

	q9 = x
	h9 = 0
	paths = []
	try:
		if h9 > 4:
			x = x/2
			q9 = x-x
			paths.append(1)
		else:
			h9 = 0-x
			h9 = h9-9
			q9 = 5/h9
			paths.append(2)
		if h9 < 9:
			x = x+8
			paths.append(3)
		else:
			x = 4-h9
			h9 = 8*h9
			q9 = 4/q9
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		q9 = h9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))