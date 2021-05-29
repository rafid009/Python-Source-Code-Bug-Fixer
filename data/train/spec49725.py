import numpy as np 

def function(x):

	u8 = x
	w9 = x
	paths = []
	try:
		if u8 < 3:
			w9 = w9-4
			u8 = 9*x
			u8 = u8/1
			paths.append(1)
		else:
			x = 3/3
			x = 2-x
			paths.append(2)
		if w9 > 8:
			u8 = 1-x
			u8 = 1-u8
			x = 6-x
			paths.append(3)
		else:
			x = x+0
			u8 = 0-u8
			u8 = 9+4
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