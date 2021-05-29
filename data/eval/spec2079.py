import numpy as np 

def function(x):

	n7 = 8
	w4 = 1
	paths = []
	try:
		if n7 < 6:
			x = x-5
			n7 = n7*7
			paths.append(1)
		else:
			n7 = 6*x
			paths.append(2)
		if x >= 7:
			x = n7*2
			n7 = n7*n7
			paths.append(3)
		else:
			n7 = 3-7
			x = 8/x
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