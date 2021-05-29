import numpy as np 

def function(x):

	h4 = 5
	h1 = x
	paths = []
	try:
		if h4 >= 9:
			h4 = 5/h4
			h4 = 8*h4
			h1 = 5-h1
			paths.append(1)
		else:
			x = 0-5
			paths.append(2)
		if x <= 1:
			h1 = 9+h1
			paths.append(3)
		else:
			h1 = h1/6
			h4 = h4*6
			h1 = 3/h1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))