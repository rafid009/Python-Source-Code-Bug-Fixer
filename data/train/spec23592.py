import numpy as np 

def function(x):

	w4 = 5
	b6 = 3
	paths = []
	try:
		if x > 2:
			w4 = w4+w4
			b6 = b6-b6
			paths.append(1)
		else:
			w4 = w4*w4
			x = x+x
			paths.append(2)
		if x >= 7:
			b6 = b6-0
			w4 = w4-w4
			paths.append(3)
		else:
			w4 = w4+x
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