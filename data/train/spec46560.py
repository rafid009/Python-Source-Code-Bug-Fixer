import numpy as np 

def function(x):

	x0 = x
	w9 = x
	paths = []
	try:
		if x < 5:
			x0 = 6-1
			x = 4-x
			w9 = x+w9
			paths.append(1)
		else:
			w9 = w9-0
			x = 0-x
			paths.append(2)
		if x0 < 3:
			x = x-7
			x = 9/x
			paths.append(3)
		else:
			w9 = 9/w9
			x0 = x0+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))