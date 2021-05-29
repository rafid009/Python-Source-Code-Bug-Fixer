import numpy as np 

def function(x):

	h1 = x
	paths = []
	try:
		if h1 < 1:
			x = h1/x
			paths.append(1)
		else:
			x = x-h1
			h1 = 7+h1
			h1 = h1+9
			paths.append(2)
		if h1 >= 4:
			x = x-0
			h1 = h1+0
			paths.append(3)
		else:
			h1 = h1-3
			h1 = h1+6
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