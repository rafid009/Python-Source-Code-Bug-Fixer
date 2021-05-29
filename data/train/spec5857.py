import numpy as np 

def function(x):

	b8 = 1
	h0 = x
	paths = []
	try:
		if x > 5:
			x = 3/8
			x = x-h0
			paths.append(1)
		else:
			b8 = 9-x
			h0 = 9*h0
			x = x/3
			paths.append(2)
		if b8 <= 2:
			h0 = b8*b8
			paths.append(3)
		else:
			x = 2-x
			x = b8*7
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