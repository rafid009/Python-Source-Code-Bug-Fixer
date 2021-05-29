import numpy as np 

def function(x):

	w4 = 3
	n4 = x
	paths = []
	try:
		if x < 4:
			x = 6+x
			n4 = 1-n4
			w4 = w4*6
			paths.append(1)
		else:
			n4 = 7-n4
			x = w4/9
			x = w4-4
			paths.append(2)
		if w4 < 4:
			w4 = w4/2
			paths.append(3)
		else:
			n4 = 9-n4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x = n4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))