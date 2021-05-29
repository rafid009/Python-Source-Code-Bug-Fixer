import numpy as np 

def function(x):

	u8 = x
	w0 = x
	paths = []
	try:
		if u8 >= 4:
			u8 = u8*x
			u8 = u8/8
			paths.append(1)
		else:
			x = w0/1
			paths.append(2)
		if w0 > 0:
			x = 9/x
			u8 = 2/3
			paths.append(3)
		else:
			u8 = 6-7
			u8 = u8-6
			x = x-w0
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