import numpy as np 

def function(x):

	u8 = x
	h1 = x
	paths = []
	try:
		if u8 < 8:
			h1 = 1+4
			h1 = x/h1
			paths.append(1)
		else:
			x = x-x
			u8 = 4+h1
			x = x-9
			paths.append(2)
		if x > 0:
			h1 = h1-h1
			x = x+8
			x = u8*x
			paths.append(3)
		else:
			h1 = h1*1
			h1 = 8+h1
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		h1 = u8**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))