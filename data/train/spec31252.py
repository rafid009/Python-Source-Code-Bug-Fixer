import numpy as np 

def function(x):

	h5 = 0
	b0 = x
	paths = []
	try:
		if b0 >= 2:
			h5 = 3-0
			h5 = h5-4
			h5 = h5*2
			paths.append(1)
		else:
			h5 = 8-2
			b0 = b0+1
			paths.append(2)
		if b0 < 2:
			h5 = h5/4
			h5 = b0/3
			x = b0/8
			paths.append(3)
		else:
			b0 = 2+b0
			h5 = h5*h5
			x = 1*x
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