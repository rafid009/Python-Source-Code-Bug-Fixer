import numpy as np 

def function(x):

	y6 = 0
	u8 = x
	paths = []
	try:
		if x <= 7:
			y6 = y6-u8
			paths.append(1)
		else:
			y6 = y6-y6
			u8 = 8/u8
			u8 = u8-0
			paths.append(2)
		if x <= 5:
			x = u8-7
			y6 = 8/1
			y6 = y6+5
			paths.append(3)
		else:
			x = x*y6
			u8 = 9+y6
			u8 = 5/7
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