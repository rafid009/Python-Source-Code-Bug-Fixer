import numpy as np 

def function(x):

	u8 = 4
	o5 = x
	paths = []
	try:
		if x > 4:
			u8 = u8/6
			paths.append(1)
		else:
			u8 = 3/u8
			x = 2/x
			paths.append(2)
		if o5 < 8:
			x = u8-0
			o5 = 3/o5
			o5 = 3+o5
			paths.append(3)
		else:
			u8 = 1/u8
			x = x*1
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		u8 = o5**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))