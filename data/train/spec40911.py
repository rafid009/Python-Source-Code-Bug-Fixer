import numpy as np 

def function(x):

	u8 = x
	d4 = x
	x = x
	paths = []
	try:
		if u8 > 2:
			x = x/6
			x = 4*u8
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if u8 <= 7:
			u8 = 6-u8
			x = 4/x
			paths.append(3)
		else:
			u8 = u8*5
			x = x-5
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		d4 = u8**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))