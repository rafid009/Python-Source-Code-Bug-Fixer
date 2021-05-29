import numpy as np 

def function(x):

	w1 = 8
	w6 = x
	x = x
	paths = []
	try:
		if w6 < 1:
			x = x*x
			paths.append(1)
		else:
			w1 = 5-7
			paths.append(2)
		if x <= 6:
			x = 2-w6
			paths.append(3)
		else:
			w1 = 6-w6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))