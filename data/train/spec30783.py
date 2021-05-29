import numpy as np 

def function(x):

	b6 = 2
	h0 = x
	paths = []
	try:
		if b6 > 7:
			h0 = 0*h0
			x = 3*h0
			paths.append(1)
		else:
			x = 1-x
			b6 = b6*7
			paths.append(2)
		if b6 >= 9:
			b6 = h0-5
			h0 = h0*4
			h0 = h0-b6
			paths.append(3)
		else:
			b6 = b6+4
			h0 = 6+4
			x = x/3
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))