import numpy as np 

def function(x):

	w4 = 2
	x4 = x
	paths = []
	try:
		if x > 5:
			x = 3-x
			w4 = 3/x
			w4 = 0/w4
			paths.append(1)
		else:
			x4 = w4/1
			x4 = x+x
			paths.append(2)
		if x > 0:
			x4 = 5-6
			paths.append(3)
		else:
			x = x4*8
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))