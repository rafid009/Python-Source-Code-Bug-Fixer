import numpy as np 

def function(x):

	w4 = x
	e9 = 7
	paths = []
	try:
		if w4 < 7:
			w4 = e9-w4
			e9 = e9+5
			e9 = e9/1
			paths.append(1)
		else:
			e9 = e9+0
			w4 = 4-w4
			w4 = w4-6
			paths.append(2)
		if w4 >= 8:
			x = x*3
			e9 = w4*e9
			paths.append(3)
		else:
			e9 = x+w4
			e9 = w4-9
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))