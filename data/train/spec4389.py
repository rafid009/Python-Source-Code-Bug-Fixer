import numpy as np 

def function(x):

	u2 = x
	h8 = x
	paths = []
	try:
		if u2 <= 4:
			h8 = 8*h8
			paths.append(1)
		else:
			h8 = h8-u2
			x = u2+x
			paths.append(2)
		if h8 <= 4:
			x = 3/x
			x = x+8
			paths.append(3)
		else:
			h8 = x/h8
			u2 = h8+0
			h8 = 9+h8
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))