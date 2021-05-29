import numpy as np 

def function(x):

	u8 = 4
	n7 = 7
	paths = []
	try:
		if x < 7:
			n7 = n7+u8
			u8 = u8-5
			n7 = 4-3
			paths.append(1)
		else:
			u8 = u8-n7
			x = x+u8
			x = u8-4
			paths.append(2)
		if x <= 8:
			x = x-1
			u8 = u8*9
			n7 = u8-8
			paths.append(3)
		else:
			n7 = 8/u8
			u8 = 5*u8
			x = x+9
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		u8 = n7**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))