import numpy as np 

def function(x):

	y5 = x
	w4 = 1
	paths = []
	try:
		if w4 >= 8:
			w4 = w4+9
			paths.append(1)
		else:
			w4 = 5-6
			x = w4/x
			paths.append(2)
		if w4 <= 6:
			y5 = 7/y5
			x = w4+w4
			x = x/1
			paths.append(3)
		else:
			w4 = 0+w4
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		w4 = y5**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))