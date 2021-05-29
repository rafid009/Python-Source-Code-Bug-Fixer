import numpy as np 

def function(x):

	y9 = 9
	h8 = 2
	paths = []
	try:
		if h8 > 2:
			x = x*8
			h8 = h8-6
			paths.append(1)
		else:
			y9 = 8+y9
			x = x+x
			paths.append(2)
		if h8 > 3:
			y9 = y9/x
			paths.append(3)
		else:
			h8 = x+h8
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))