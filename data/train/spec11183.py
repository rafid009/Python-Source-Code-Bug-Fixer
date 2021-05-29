import numpy as np 

def function(x):

	x0 = x
	u8 = x
	x = x
	paths = []
	try:
		if x > 2:
			x0 = x0+8
			u8 = u8+x
			x0 = 3+x0
			paths.append(1)
		else:
			u8 = u8+x
			u8 = u8/x
			paths.append(2)
		if x < 8:
			u8 = 3+u8
			paths.append(3)
		else:
			x0 = x+0
			x0 = x0-2
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))