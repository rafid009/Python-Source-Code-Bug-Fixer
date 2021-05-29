import numpy as np 

def function(x):

	b8 = x
	h0 = x
	paths = []
	try:
		if b8 >= 1:
			x = 4*h0
			x = x+2
			paths.append(1)
		else:
			b8 = 6+4
			x = b8*b8
			h0 = 3*h0
			paths.append(2)
		if h0 > 5:
			h0 = h0-6
			h0 = 2/8
			paths.append(3)
		else:
			b8 = b8*8
			h0 = 3-x
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		b8 = h0**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))