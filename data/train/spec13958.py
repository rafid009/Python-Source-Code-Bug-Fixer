import numpy as np 

def function(x):

	l6 = 8
	w4 = 3
	paths = []
	try:
		if l6 <= 1:
			l6 = x-5
			w4 = w4/3
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if l6 < 8:
			x = x-4
			paths.append(3)
		else:
			x = l6-w4
			x = x-8
			l6 = l6-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))