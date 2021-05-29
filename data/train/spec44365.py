import numpy as np 

def function(x):

	h7 = x
	q9 = x
	paths = []
	try:
		if x > 0:
			h7 = 5-8
			paths.append(1)
		else:
			h7 = q9-7
			x = 8-x
			paths.append(2)
		if x > 1:
			q9 = h7/q9
			h7 = h7-2
			x = 7-9
			paths.append(3)
		else:
			h7 = 3/5
			q9 = q9*5
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))