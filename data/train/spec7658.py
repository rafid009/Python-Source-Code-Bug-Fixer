import numpy as np 

def function(x):

	l9 = 3
	w9 = x
	paths = []
	try:
		if w9 >= 2:
			l9 = l9-8
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if l9 <= 6:
			w9 = w9+8
			x = 8+x
			x = x-3
			paths.append(3)
		else:
			w9 = l9*w9
			l9 = 1/l9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))