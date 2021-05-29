import numpy as np 

def function(x):

	h8 = x
	n8 = x
	paths = []
	try:
		if n8 < 6:
			n8 = 6-7
			n8 = h8*8
			x = x+x
			paths.append(1)
		else:
			n8 = n8+h8
			h8 = h8+8
			h8 = 4*n8
			paths.append(2)
		if x > 9:
			h8 = n8*h8
			paths.append(3)
		else:
			n8 = n8*n8
			n8 = n8+h8
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