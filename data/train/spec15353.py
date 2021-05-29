import numpy as np 

def function(x):

	u8 = 8
	d0 = x
	paths = []
	try:
		if d0 > 7:
			d0 = d0-x
			paths.append(1)
		else:
			x = x*u8
			u8 = x+2
			u8 = x+x
			paths.append(2)
		if d0 > 7:
			x = 0*d0
			u8 = 7*u8
			paths.append(3)
		else:
			d0 = u8*x
			d0 = 6-2
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		d0 = u8**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))