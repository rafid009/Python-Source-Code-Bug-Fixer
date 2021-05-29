import numpy as np 

def function(x):

	y1 = x
	h2 = 2
	paths = []
	try:
		if y1 >= 2:
			y1 = y1+1
			paths.append(1)
		else:
			x = y1/h2
			x = 2+y1
			paths.append(2)
		if h2 <= 0:
			y1 = 0-y1
			h2 = 7/h2
			paths.append(3)
		else:
			h2 = 5-9
			y1 = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))