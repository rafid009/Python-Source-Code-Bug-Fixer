import numpy as np 

def function(x):

	h0 = 6
	b9 = x
	paths = []
	try:
		if b9 >= 2:
			b9 = 6-b9
			paths.append(1)
		else:
			b9 = 6+2
			b9 = 8-h0
			paths.append(2)
		if x < 9:
			x = x/x
			paths.append(3)
		else:
			h0 = h0-0
			h0 = b9+8
			b9 = 6*b9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))