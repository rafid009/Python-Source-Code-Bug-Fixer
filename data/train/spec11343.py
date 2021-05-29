import numpy as np 

def function(x):

	u8 = x
	d8 = x
	x = x
	paths = []
	try:
		if d8 < 6:
			d8 = 8-5
			d8 = d8+0
			x = x*d8
			paths.append(1)
		else:
			u8 = u8*d8
			paths.append(2)
		if d8 >= 9:
			u8 = x+u8
			paths.append(3)
		else:
			d8 = d8*3
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		d8 = u8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))