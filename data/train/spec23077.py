import numpy as np 

def function(x):

	h0 = x
	y9 = x
	paths = []
	try:
		if y9 > 4:
			x = x/1
			h0 = y9+6
			paths.append(1)
		else:
			y9 = 3-y9
			paths.append(2)
		if y9 <= 4:
			y9 = 8*y9
			h0 = h0*0
			h0 = h0*9
			paths.append(3)
		else:
			y9 = h0/y9
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		h0 = h0**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))