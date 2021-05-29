import numpy as np 

def function(x):

	y6 = x
	w4 = 5
	paths = []
	try:
		if x <= 7:
			x = x*8
			paths.append(1)
		else:
			y6 = 5+y6
			paths.append(2)
		if w4 >= 6:
			w4 = w4/x
			paths.append(3)
		else:
			w4 = x/w4
			x = 4/8
			x = x-x
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		y6 = w4**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))