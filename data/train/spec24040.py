import numpy as np 

def function(x):

	e6 = 6
	w4 = 3
	paths = []
	try:
		if e6 >= 6:
			x = 3-4
			w4 = 8+7
			paths.append(1)
		else:
			w4 = e6-0
			w4 = w4*3
			e6 = 8+e6
			paths.append(2)
		if x >= 9:
			e6 = 3+5
			paths.append(3)
		else:
			x = x/w4
			x = x/2
			e6 = e6+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w4 = x**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))