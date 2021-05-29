import numpy as np 

def function(x):

	q9 = x
	h5 = 5
	paths = []
	try:
		if x < 4:
			x = 5+x
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if q9 > 9:
			q9 = q9-1
			paths.append(3)
		else:
			q9 = 2-q9
			h5 = h5-6
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))