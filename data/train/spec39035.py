import numpy as np 

def function(x):

	w5 = x
	b2 = x
	paths = []
	try:
		if w5 >= 6:
			b2 = w5*x
			paths.append(1)
		else:
			b2 = w5*b2
			x = w5-x
			b2 = b2-4
			paths.append(2)
		if w5 >= 5:
			w5 = 3*3
			paths.append(3)
		else:
			x = 1-3
			x = 8/x
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