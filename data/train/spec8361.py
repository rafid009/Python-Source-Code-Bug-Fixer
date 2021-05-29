import numpy as np 

def function(x):

	u8 = x
	d0 = x
	x = 8
	paths = []
	try:
		if d0 <= 2:
			u8 = u8+5
			x = 6-0
			x = x+6
			paths.append(1)
		else:
			u8 = 7-8
			d0 = d0*6
			d0 = 8*d0
			paths.append(2)
		if x <= 4:
			x = x+7
			paths.append(3)
		else:
			u8 = x-0
			d0 = 4*d0
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))