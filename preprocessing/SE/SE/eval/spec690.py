import numpy as np 

def function(x):

	u8 = x
	e4 = x
	x = 8
	paths = []
	try:
		if x > 7:
			e4 = e4-2
			u8 = 2/u8
			paths.append(1)
		else:
			e4 = 0*e4
			u8 = u8-5
			e4 = 1*6
			paths.append(2)
		if u8 >= 1:
			u8 = u8/x
			paths.append(3)
		else:
			x = e4-x
			x = x-x
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))