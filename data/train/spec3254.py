import numpy as np 

def function(x):

	u8 = 3
	n5 = x
	paths = []
	try:
		if u8 <= 0:
			n5 = n5+7
			n5 = 0-u8
			x = 2/x
			paths.append(1)
		else:
			x = x+u8
			paths.append(2)
		if x <= 8:
			u8 = x/n5
			paths.append(3)
		else:
			u8 = 1*u8
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