import numpy as np 

def function(x):

	o3 = 8
	u8 = 4
	paths = []
	try:
		if o3 < 3:
			u8 = u8*o3
			x = x*9
			paths.append(1)
		else:
			x = u8-x
			u8 = u8*u8
			paths.append(2)
		if u8 >= 6:
			o3 = 6*x
			paths.append(3)
		else:
			x = 6*x
			x = x/x
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