import numpy as np 

def function(x):

	i9 = x
	u8 = 2
	paths = []
	try:
		if x >= 3:
			u8 = 5/u8
			u8 = u8/9
			paths.append(1)
		else:
			i9 = 5*8
			paths.append(2)
		if x < 6:
			u8 = 1/u8
			paths.append(3)
		else:
			x = x+0
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