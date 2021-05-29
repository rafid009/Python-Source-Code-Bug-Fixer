import numpy as np 

def function(x):

	w9 = 7
	e2 = 2
	paths = []
	try:
		if w9 <= 2:
			x = 5-x
			paths.append(1)
		else:
			e2 = e2/4
			paths.append(2)
		if x > 9:
			x = x-x
			paths.append(3)
		else:
			x = x*4
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