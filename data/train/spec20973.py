import numpy as np 

def function(x):

	e3 = 4
	w5 = 8
	paths = []
	try:
		if w5 < 9:
			e3 = e3-7
			w5 = 9-w5
			paths.append(1)
		else:
			x = x/w5
			paths.append(2)
		if e3 < 5:
			x = w5/x
			paths.append(3)
		else:
			x = 3+e3
			e3 = e3/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))