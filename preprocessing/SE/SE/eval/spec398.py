import numpy as np 

def function(x):

	w7 = 2
	q8 = 6
	paths = []
	try:
		if x <= 9:
			w7 = w7/8
			w7 = w7-3
			paths.append(1)
		else:
			x = 2/x
			x = 7+0
			paths.append(2)
		if q8 < 0:
			w7 = w7-4
			paths.append(3)
		else:
			x = 4*2
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))