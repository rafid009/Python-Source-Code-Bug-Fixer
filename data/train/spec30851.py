import numpy as np 

def function(x):

	l8 = 1
	w6 = 0
	paths = []
	try:
		if w6 <= 0:
			l8 = l8+9
			w6 = x/8
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if w6 <= 8:
			x = 4-l8
			x = x*1
			l8 = l8/w6
			paths.append(3)
		else:
			l8 = 8-l8
			l8 = w6-3
			x = x+2
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