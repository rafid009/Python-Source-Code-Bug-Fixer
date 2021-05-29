import numpy as np 

def function(x):

	h0 = x
	b7 = x
	paths = []
	try:
		if x > 8:
			x = 9-x
			paths.append(1)
		else:
			x = 6*x
			b7 = 4+b7
			h0 = h0-7
			paths.append(2)
		if h0 > 4:
			b7 = 3/b7
			x = x*4
			x = x-0
			paths.append(3)
		else:
			b7 = 8-b7
			x = 0+3
			h0 = 0-h0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))