import numpy as np 

def function(x):

	u8 = x
	f5 = x
	paths = []
	try:
		if u8 > 6:
			u8 = u8-f5
			paths.append(1)
		else:
			f5 = u8-3
			f5 = 8+f5
			f5 = x-7
			paths.append(2)
		if f5 <= 2:
			x = 4-x
			f5 = 9/f5
			paths.append(3)
		else:
			x = 6/x
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