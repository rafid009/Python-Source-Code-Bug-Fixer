import numpy as np 

def function(x):

	h1 = 8
	r6 = 2
	paths = []
	try:
		if x < 8:
			r6 = 5/5
			h1 = r6-1
			paths.append(1)
		else:
			h1 = h1*7
			paths.append(2)
		if h1 < 1:
			h1 = r6/1
			paths.append(3)
		else:
			h1 = h1/5
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