import numpy as np 

def function(x):

	u8 = x
	o7 = 5
	x = x
	paths = []
	try:
		if u8 >= 9:
			x = x+4
			o7 = o7/7
			paths.append(1)
		else:
			u8 = u8*3
			u8 = u8-9
			o7 = o7-6
			paths.append(2)
		if x < 8:
			o7 = 5+o7
			u8 = u8+2
			paths.append(3)
		else:
			x = x/6
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