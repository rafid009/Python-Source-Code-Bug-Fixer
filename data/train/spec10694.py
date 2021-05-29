import numpy as np 

def function(x):

	u8 = x
	v4 = 7
	paths = []
	try:
		if u8 > 3:
			u8 = u8+0
			v4 = v4+8
			paths.append(1)
		else:
			u8 = 0/u8
			u8 = v4*u8
			paths.append(2)
		if v4 < 1:
			u8 = u8/v4
			u8 = u8/5
			paths.append(3)
		else:
			x = x/8
			v4 = v4/9
			x = u8+x
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