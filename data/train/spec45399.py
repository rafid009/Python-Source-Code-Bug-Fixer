import numpy as np 

def function(x):

	x4 = 8
	w7 = x
	paths = []
	try:
		if x4 > 4:
			x4 = x4+8
			w7 = w7*7
			paths.append(1)
		else:
			w7 = w7-8
			x = x-1
			paths.append(2)
		if x >= 2:
			w7 = w7*w7
			x4 = 4-x4
			paths.append(3)
		else:
			x4 = x4/1
			x = 5/2
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		w7 = x4**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))