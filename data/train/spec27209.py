import numpy as np 

def function(x):

	d1 = 4
	u8 = 0
	paths = []
	try:
		if x <= 3:
			d1 = 2-d1
			u8 = x-d1
			paths.append(1)
		else:
			u8 = u8-d1
			u8 = 8/9
			paths.append(2)
		if x >= 4:
			x = x+d1
			x = x-6
			x = 8-x
			paths.append(3)
		else:
			d1 = x/d1
			u8 = u8*d1
			d1 = x*u8
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))