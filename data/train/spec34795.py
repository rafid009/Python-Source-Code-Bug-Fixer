import numpy as np 

def function(x):

	q4 = 8
	h1 = 2
	paths = []
	try:
		if q4 <= 6:
			q4 = 3*h1
			paths.append(1)
		else:
			h1 = h1+0
			q4 = q4/6
			q4 = q4-2
			paths.append(2)
		if h1 >= 7:
			x = 5*8
			q4 = q4*q4
			paths.append(3)
		else:
			q4 = 8*q4
			q4 = 0-q4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))