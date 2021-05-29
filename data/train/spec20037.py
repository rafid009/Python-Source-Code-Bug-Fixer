import numpy as np 

def function(x):

	u8 = x
	x7 = 2
	paths = []
	try:
		if x7 > 1:
			x7 = x+u8
			u8 = u8-6
			paths.append(1)
		else:
			x7 = u8*x7
			x = 6+8
			x7 = x7+2
			paths.append(2)
		if x7 > 8:
			x = 2+x7
			paths.append(3)
		else:
			x7 = u8+8
			u8 = u8-6
			x = 6+u8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		u8 = u8**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))