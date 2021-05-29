import numpy as np 

def function(x):

	p3 = 6
	w8 = x
	paths = []
	try:
		if x >= 9:
			w8 = 4-w8
			paths.append(1)
		else:
			w8 = x-x
			paths.append(2)
		if w8 < 0:
			x = 5*x
			w8 = w8*p3
			paths.append(3)
		else:
			x = x+7
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