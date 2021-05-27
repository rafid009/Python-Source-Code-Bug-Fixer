import numpy as np 

def function(x):

	h8 = x
	b5 = x
	paths = []
	try:
		if h8 < 0:
			b5 = 9-x
			x = h8-1
			b5 = b5+x
			paths.append(1)
		else:
			b5 = b5*b5
			paths.append(2)
		if h8 >= 8:
			h8 = 8*h8
			paths.append(3)
		else:
			b5 = 7+8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		b5 = h8**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))