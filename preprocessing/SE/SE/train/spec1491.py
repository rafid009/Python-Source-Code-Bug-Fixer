import numpy as np 

def function(x):

	w9 = 3
	e0 = 2
	paths = []
	try:
		if x < 1:
			x = x*7
			x = x/4
			w9 = 0/w9
			paths.append(1)
		else:
			w9 = w9*1
			paths.append(2)
		if x >= 0:
			e0 = e0/e0
			x = 2-x
			e0 = 2-e0
			paths.append(3)
		else:
			w9 = w9*5
			e0 = e0-2
			e0 = 5-e0
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