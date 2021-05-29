import numpy as np 

def function(x):

	t0 = x
	u8 = x
	paths = []
	try:
		if u8 >= 9:
			t0 = t0/5
			u8 = 0+6
			x = u8-x
			paths.append(1)
		else:
			u8 = t0-u8
			paths.append(2)
		if u8 < 6:
			u8 = 2+u8
			paths.append(3)
		else:
			x = x-9
			t0 = 0+u8
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