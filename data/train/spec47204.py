import numpy as np 

def function(x):

	e0 = 8
	w9 = 1
	paths = []
	try:
		if x > 2:
			e0 = w9/e0
			x = e0-4
			paths.append(1)
		else:
			e0 = w9-8
			paths.append(2)
		if e0 <= 6:
			x = 1-1
			w9 = w9/6
			paths.append(3)
		else:
			x = 3+x
			e0 = 7/x
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		w9 = e0**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))