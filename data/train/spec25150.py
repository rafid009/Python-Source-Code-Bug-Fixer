import numpy as np 

def function(x):

	y3 = x
	w4 = x
	paths = []
	try:
		if x > 6:
			x = 0-x
			y3 = y3/x
			paths.append(1)
		else:
			y3 = 5-5
			w4 = y3/2
			paths.append(2)
		if x > 5:
			w4 = w4-7
			paths.append(3)
		else:
			y3 = y3+7
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