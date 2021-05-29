import numpy as np 

def function(x):

	u8 = x
	u7 = 7
	paths = []
	try:
		if u7 > 2:
			x = 8+x
			x = 8/7
			u7 = u7-7
			paths.append(1)
		else:
			u8 = 8*u8
			x = x/4
			paths.append(2)
		if u8 < 0:
			x = 5-x
			paths.append(3)
		else:
			x = x*u7
			u8 = 3/u8
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