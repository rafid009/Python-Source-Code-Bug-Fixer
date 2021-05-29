import numpy as np 

def function(x):

	u8 = x
	w4 = 3
	x = 7
	paths = []
	try:
		if w4 >= 1:
			x = 4/x
			u8 = u8+8
			u8 = u8*9
			paths.append(1)
		else:
			u8 = u8+1
			x = x*4
			paths.append(2)
		if w4 <= 2:
			x = x/u8
			paths.append(3)
		else:
			x = 2/8
			w4 = 1-w4
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		w4 = u8**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))