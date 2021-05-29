import numpy as np 

def function(x):

	h2 = 3
	q5 = 6
	paths = []
	try:
		if x >= 8:
			x = x-x
			x = 1-x
			q5 = 1-2
			paths.append(1)
		else:
			h2 = h2-x
			paths.append(2)
		if x > 3:
			x = h2/x
			h2 = x-h2
			paths.append(3)
		else:
			x = 4/x
			q5 = q5/x
			q5 = h2/q5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))