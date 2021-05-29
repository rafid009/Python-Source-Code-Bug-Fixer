import numpy as np 

def function(x):

	h5 = x
	q9 = 1
	paths = []
	try:
		if x > 5:
			x = x+q9
			q9 = 4+q9
			paths.append(1)
		else:
			h5 = h5+3
			q9 = q9-q9
			paths.append(2)
		if x < 1:
			x = q9+7
			paths.append(3)
		else:
			h5 = 6*h5
			q9 = q9*2
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		h5 = h5**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))