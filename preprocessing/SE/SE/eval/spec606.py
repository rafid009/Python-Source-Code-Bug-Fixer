import numpy as np 

def function(x):

	w4 = 3
	w6 = x
	paths = []
	try:
		if x <= 1:
			x = x-w6
			paths.append(1)
		else:
			x = 4+x
			x = x-8
			paths.append(2)
		if w6 <= 6:
			w6 = w4-6
			paths.append(3)
		else:
			w6 = 9/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))