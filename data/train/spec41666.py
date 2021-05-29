import numpy as np 

def function(x):

	a7 = 6
	w6 = x
	paths = []
	try:
		if x > 5:
			w6 = a7+4
			a7 = a7*4
			w6 = w6*a7
			paths.append(1)
		else:
			a7 = 0-w6
			x = w6+x
			paths.append(2)
		if w6 >= 1:
			x = 0/x
			x = 8-w6
			paths.append(3)
		else:
			x = x-3
			a7 = a7-2
			x = a7*x
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