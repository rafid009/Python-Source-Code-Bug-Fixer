import numpy as np 

def function(x):

	o8 = 3
	u8 = x
	x = x
	paths = []
	try:
		if u8 < 8:
			x = 7*x
			paths.append(1)
		else:
			u8 = u8/o8
			o8 = 3/o8
			paths.append(2)
		if o8 >= 3:
			o8 = x-u8
			x = x-8
			o8 = o8/6
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		u8 = o8**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))