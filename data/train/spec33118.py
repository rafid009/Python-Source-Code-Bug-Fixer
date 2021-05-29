import numpy as np 

def function(x):

	q9 = 3
	h9 = 9
	paths = []
	try:
		if q9 > 9:
			q9 = h9/2
			x = x-4
			paths.append(1)
		else:
			x = x*7
			x = x-q9
			paths.append(2)
		if x < 9:
			h9 = q9/1
			paths.append(3)
		else:
			q9 = x-q9
			x = x-4
			h9 = 9*h9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))