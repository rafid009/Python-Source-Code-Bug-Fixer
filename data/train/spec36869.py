import numpy as np 

def function(x):

	h0 = x
	i2 = x
	paths = []
	try:
		if h0 < 0:
			h0 = i2*h0
			x = 3-4
			paths.append(1)
		else:
			h0 = h0+3
			paths.append(2)
		if i2 >= 9:
			x = 8+x
			x = 4+0
			h0 = h0*4
			paths.append(3)
		else:
			x = x/1
			i2 = 9-2
			h0 = 1*h0
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