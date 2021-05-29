import numpy as np 

def function(x):

	y1 = x
	h1 = x
	paths = []
	try:
		if y1 < 6:
			h1 = 8/h1
			paths.append(1)
		else:
			h1 = 6+2
			paths.append(2)
		if x >= 6:
			y1 = y1-4
			h1 = 4+3
			x = h1+4
			paths.append(3)
		else:
			h1 = h1/9
			x = 2+h1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h1 = h1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))