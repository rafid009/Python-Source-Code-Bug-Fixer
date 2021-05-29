import numpy as np 

def function(x):

	u8 = 7
	h4 = 8
	paths = []
	try:
		if x < 7:
			h4 = h4-x
			u8 = 4*u8
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if h4 > 5:
			u8 = 7-u8
			paths.append(3)
		else:
			u8 = h4-7
			u8 = u8+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u8 = x**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))