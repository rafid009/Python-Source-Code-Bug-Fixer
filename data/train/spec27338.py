import numpy as np 

def function(x):

	h1 = 4
	b4 = x
	paths = []
	try:
		if b4 < 6:
			h1 = 8/2
			h1 = h1*h1
			paths.append(1)
		else:
			h1 = 0/2
			b4 = b4*5
			paths.append(2)
		if b4 > 6:
			x = 6/6
			b4 = 3*b4
			x = x*b4
			paths.append(3)
		else:
			h1 = 8-x
			x = x/x
			b4 = b4/8
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))