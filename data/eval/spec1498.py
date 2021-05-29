import numpy as np 

def function(x):

	w8 = 6
	e8 = 6
	paths = []
	try:
		if e8 <= 8:
			w8 = w8*w8
			e8 = e8+3
			x = x/1
			paths.append(1)
		else:
			e8 = 3/5
			paths.append(2)
		if x > 2:
			x = 7+x
			x = x-x
			paths.append(3)
		else:
			e8 = 1/e8
			e8 = 8-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))