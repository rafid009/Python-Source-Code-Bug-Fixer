import numpy as np 

def function(x):

	d5 = x
	u8 = x
	paths = []
	try:
		if x > 2:
			d5 = d5+u8
			x = d5/4
			d5 = d5*1
			paths.append(1)
		else:
			u8 = d5/u8
			d5 = 9-6
			u8 = u8*x
			paths.append(2)
		if d5 < 3:
			d5 = 0+4
			paths.append(3)
		else:
			u8 = 4-u8
			d5 = 1+5
			u8 = d5+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u8 = x**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))