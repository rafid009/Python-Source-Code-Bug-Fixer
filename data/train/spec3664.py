import numpy as np 

def function(x):

	e7 = 2
	w4 = x
	paths = []
	try:
		if w4 <= 6:
			e7 = 8-w4
			e7 = 8-e7
			e7 = e7*e7
			paths.append(1)
		else:
			x = x/e7
			x = x-9
			paths.append(2)
		if e7 >= 9:
			e7 = e7+e7
			w4 = e7*3
			paths.append(3)
		else:
			w4 = x+x
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		e7 = w4**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))