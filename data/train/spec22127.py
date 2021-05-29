import numpy as np 

def function(x):

	y8 = 5
	u8 = x
	paths = []
	try:
		if x >= 5:
			u8 = u8-x
			u8 = 2-3
			paths.append(1)
		else:
			u8 = u8*0
			x = x-2
			paths.append(2)
		if y8 >= 7:
			y8 = y8/2
			u8 = u8*x
			u8 = u8+9
			paths.append(3)
		else:
			x = 8-x
			y8 = 6*y8
			x = 7/3
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))