import numpy as np 

def function(x):

	w4 = x
	a8 = x
	paths = []
	try:
		if w4 > 4:
			a8 = a8*w4
			paths.append(1)
		else:
			x = 2-x
			x = w4+5
			a8 = a8-4
			paths.append(2)
		if w4 <= 1:
			x = x-6
			x = x+x
			paths.append(3)
		else:
			w4 = a8*1
			a8 = w4/a8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))