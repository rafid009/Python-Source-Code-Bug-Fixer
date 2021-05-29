import numpy as np 

def function(x):

	h6 = 2
	b0 = x
	paths = []
	try:
		if x < 4:
			b0 = 8+b0
			paths.append(1)
		else:
			h6 = h6*4
			h6 = h6-1
			paths.append(2)
		if b0 > 8:
			x = b0-x
			paths.append(3)
		else:
			x = 6+x
			h6 = 7*b0
			x = h6+x
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))