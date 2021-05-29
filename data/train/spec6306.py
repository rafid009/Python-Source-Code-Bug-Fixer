import numpy as np 

def function(x):

	v7 = 4
	u8 = x
	paths = []
	try:
		if x <= 8:
			x = 6/4
			x = v7/u8
			v7 = v7-6
			paths.append(1)
		else:
			v7 = 5+2
			u8 = u8-6
			x = x/x
			paths.append(2)
		if x > 9:
			x = 6+x
			u8 = u8/9
			paths.append(3)
		else:
			v7 = v7-u8
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