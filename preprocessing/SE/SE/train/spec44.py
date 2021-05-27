import numpy as np 

def function(x):

	h1 = x
	h7 = 9
	paths = []
	try:
		if h1 <= 9:
			h1 = h1/2
			h1 = x+h1
			h7 = h7*8
			paths.append(1)
		else:
			x = x-2
			h7 = h1/h7
			h1 = 1/7
			paths.append(2)
		if h1 >= 4:
			h7 = h7-2
			h1 = h1+7
			h7 = h7/4
			paths.append(3)
		else:
			h7 = 7-1
			h1 = 4*h1
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