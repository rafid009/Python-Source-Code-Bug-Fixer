import numpy as np 

def function(x):

	e9 = x
	w8 = x
	paths = []
	try:
		if x >= 3:
			x = 9-x
			paths.append(1)
		else:
			e9 = 2+w8
			x = 2*x
			paths.append(2)
		if w8 < 2:
			x = 1+0
			w8 = w8*1
			paths.append(3)
		else:
			w8 = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))