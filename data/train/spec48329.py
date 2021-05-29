import numpy as np 

def function(x):

	e6 = 0
	w4 = 1
	paths = []
	try:
		if w4 > 9:
			w4 = w4*x
			x = 5-1
			paths.append(1)
		else:
			e6 = 6+0
			w4 = 3/2
			w4 = 4/w4
			paths.append(2)
		if e6 < 7:
			w4 = 6/w4
			paths.append(3)
		else:
			w4 = 7+w4
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