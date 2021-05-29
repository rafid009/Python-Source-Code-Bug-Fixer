import numpy as np 

def function(x):

	n4 = 7
	w7 = 3
	paths = []
	try:
		if n4 < 8:
			x = x-0
			n4 = n4-8
			x = x-8
			paths.append(1)
		else:
			w7 = w7/9
			x = w7/x
			paths.append(2)
		if w7 < 5:
			n4 = n4/9
			x = x-4
			n4 = n4-w7
			paths.append(3)
		else:
			w7 = 4*w7
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