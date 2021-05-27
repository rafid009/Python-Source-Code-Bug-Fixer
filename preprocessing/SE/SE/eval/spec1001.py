import numpy as np 

def function(x):

	d4 = 3
	u8 = x
	paths = []
	try:
		if d4 > 0:
			u8 = x*u8
			u8 = 6-7
			paths.append(1)
		else:
			d4 = 5-d4
			d4 = d4+x
			u8 = 4/u8
			paths.append(2)
		if d4 < 9:
			d4 = 2/4
			paths.append(3)
		else:
			u8 = 4+u8
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