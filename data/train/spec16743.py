import numpy as np 

def function(x):

	h3 = x
	h1 = 2
	paths = []
	try:
		if h3 < 3:
			h1 = h1*6
			h1 = x+h3
			h1 = 1+h1
			paths.append(1)
		else:
			x = 1*3
			paths.append(2)
		if x <= 7:
			h1 = 7-h1
			x = x-4
			paths.append(3)
		else:
			x = x/1
			x = x+4
			h1 = h1-0
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h1 = h3**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))