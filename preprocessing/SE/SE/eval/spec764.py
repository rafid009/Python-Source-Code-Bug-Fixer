import numpy as np 

def function(x):

	u8 = x
	d1 = 9
	x = 7
	paths = []
	try:
		if u8 <= 2:
			x = d1/9
			u8 = u8+x
			u8 = u8/7
			paths.append(1)
		else:
			d1 = 3-d1
			paths.append(2)
		if x >= 3:
			u8 = 0*u8
			x = x-8
			x = x-u8
			paths.append(3)
		else:
			x = u8*5
			x = x/x
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		d1 = u8**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))