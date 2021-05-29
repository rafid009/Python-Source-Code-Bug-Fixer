import numpy as np 

def function(x):

	h9 = x
	q8 = 9
	paths = []
	try:
		if x < 7:
			h9 = 9*h9
			q8 = 5/q8
			h9 = 6+3
			paths.append(1)
		else:
			h9 = 8-h9
			q8 = q8-1
			h9 = x*h9
			paths.append(2)
		if x <= 5:
			x = h9+1
			q8 = 5-7
			paths.append(3)
		else:
			q8 = x-q8
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		q8 = h9**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))