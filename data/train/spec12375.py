import numpy as np 

def function(x):

	q6 = x
	h1 = 8
	paths = []
	try:
		if x > 3:
			q6 = q6-q6
			paths.append(1)
		else:
			q6 = 1+0
			h1 = 3-7
			paths.append(2)
		if h1 > 9:
			x = h1/6
			h1 = 6*h1
			x = q6/q6
			paths.append(3)
		else:
			h1 = 6+0
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