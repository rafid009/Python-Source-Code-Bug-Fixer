import numpy as np 

def function(x):

	u8 = x
	o5 = x
	paths = []
	try:
		if u8 >= 9:
			u8 = u8-u8
			o5 = 5+o5
			paths.append(1)
		else:
			o5 = o5+5
			paths.append(2)
		if o5 <= 2:
			u8 = 5+u8
			x = x-x
			paths.append(3)
		else:
			x = 5/x
			o5 = u8-4
			u8 = 3*3
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