import numpy as np 

def function(x):

	u8 = 0
	u4 = x
	paths = []
	try:
		if u8 >= 6:
			x = x/9
			x = 0/u8
			paths.append(1)
		else:
			u4 = 5+7
			x = x+6
			x = 5-x
			paths.append(2)
		if u8 >= 2:
			x = x-u4
			u4 = u4+u4
			u4 = 7/x
			paths.append(3)
		else:
			u4 = 9-u4
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x = u4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))