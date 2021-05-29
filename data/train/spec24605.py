import numpy as np 

def function(x):

	u8 = x
	l8 = 5
	paths = []
	try:
		if x >= 9:
			u8 = 0+u8
			x = x+u8
			paths.append(1)
		else:
			u8 = u8/l8
			l8 = 1-l8
			l8 = 4*4
			paths.append(2)
		if x <= 1:
			x = 7+x
			paths.append(3)
		else:
			l8 = 6/x
			u8 = u8/u8
			u8 = 0*u8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		l8 = u8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))