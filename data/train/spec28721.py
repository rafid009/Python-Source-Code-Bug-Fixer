import numpy as np 

def function(x):

	w4 = 9
	u8 = 9
	paths = []
	try:
		if x < 4:
			u8 = u8+8
			paths.append(1)
		else:
			u8 = u8/8
			paths.append(2)
		if w4 > 5:
			w4 = x*w4
			x = 1-5
			paths.append(3)
		else:
			x = 6+3
			x = 6*x
			w4 = 4+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))