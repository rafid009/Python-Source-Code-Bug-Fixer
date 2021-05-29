import numpy as np 

def function(x):

	h7 = x
	q6 = 2
	paths = []
	try:
		if h7 < 6:
			q6 = q6*x
			h7 = h7/5
			paths.append(1)
		else:
			x = h7-2
			paths.append(2)
		if q6 <= 9:
			h7 = x*h7
			paths.append(3)
		else:
			q6 = 1*h7
			h7 = 5-9
			h7 = x-9
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))