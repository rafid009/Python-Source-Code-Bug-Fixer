import numpy as np 

def function(x):

	u8 = 8
	e4 = x
	paths = []
	try:
		if u8 < 7:
			u8 = e4*x
			x = 3*x
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if u8 >= 3:
			e4 = 4/e4
			u8 = 2-8
			e4 = 8/e4
			paths.append(3)
		else:
			u8 = 0*u8
			x = 8-x
			x = x-8
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		u8 = e4**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))