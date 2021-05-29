import numpy as np 

def function(x):

	q9 = x
	h6 = x
	paths = []
	try:
		if x <= 6:
			h6 = h6*9
			h6 = 0-h6
			q9 = h6/5
			paths.append(1)
		else:
			q9 = q9*9
			x = x+h6
			q9 = 2*h6
			paths.append(2)
		if h6 < 6:
			x = h6-7
			paths.append(3)
		else:
			x = 8+7
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))