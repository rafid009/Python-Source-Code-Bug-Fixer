import numpy as np 

def function(x):

	w0 = x
	u8 = x
	paths = []
	try:
		if u8 < 0:
			w0 = w0+x
			paths.append(1)
		else:
			x = u8+0
			u8 = u8+8
			paths.append(2)
		if u8 > 5:
			w0 = 7+w0
			u8 = 7/u8
			paths.append(3)
		else:
			w0 = w0-2
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		w0 = u8**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))