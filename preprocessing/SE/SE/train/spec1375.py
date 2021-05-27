import numpy as np 

def function(x):

	h8 = x
	h1 = x
	paths = []
	try:
		if h1 <= 4:
			h1 = h1/h1
			paths.append(1)
		else:
			h8 = h1*h1
			h8 = h8/6
			x = h1-5
			paths.append(2)
		if h1 <= 0:
			h1 = h1*8
			h1 = h1+x
			x = 3*h8
			paths.append(3)
		else:
			h1 = 5/h1
			h1 = h1-4
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h8 = h1**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))