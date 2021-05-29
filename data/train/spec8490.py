import numpy as np 

def function(x):

	q9 = x
	h3 = x
	paths = []
	try:
		if x >= 6:
			q9 = q9-q9
			q9 = q9*7
			paths.append(1)
		else:
			q9 = q9/3
			h3 = x-9
			paths.append(2)
		if q9 <= 7:
			x = 3/x
			x = x/5
			paths.append(3)
		else:
			h3 = 3-3
			q9 = 9-5
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		x = h3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))