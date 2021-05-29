import numpy as np 

def function(x):

	w4 = x
	y8 = x
	paths = []
	try:
		if y8 >= 8:
			x = 8+x
			y8 = 4-y8
			paths.append(1)
		else:
			w4 = w4*9
			w4 = 5+x
			paths.append(2)
		if w4 < 6:
			y8 = w4/w4
			x = w4/x
			w4 = w4-8
			paths.append(3)
		else:
			w4 = w4/x
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))